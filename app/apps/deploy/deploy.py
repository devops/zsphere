#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import json

import tornado.web

from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.options import options

from app.base import BaseHandler

class DeployHandler(BaseHandler):
    def get(self):
        #self.render('deploys/index.html', items=dict())
        self.redirect("/deploys/project")

class ProjectHandler(BaseHandler):

    @gen.coroutine
    def get(self, *args, **kwargs):
        url = options.BASE_URL + '/api/v1/deploys/projects'
        client = AsyncHTTPClient()
        response = yield client.fetch(url)
        if response.body:
            body = json.loads(response.body)
        else:
            body = {}

        self.render('deploys/project/index.html', items=body)

class ProjectAddHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("deploys/project/add.html", items=dict())

    @tornado.web.authenticated
    @gen.coroutine
    def post(self, *args, **kwargs):
        params = ('project', 'description', 'group')
        item = dict()
        for param in params:
            item[param] = self.get_argument(param, '')
        item['create_by'] = self.get_current_user()
        url = options.BASE_URL + '/api/v1/deploys/projects'
        request = HTTPRequest(url, method="POST", body=json.dumps(item))
        client = AsyncHTTPClient()
        response = yield client.fetch(request)
        self.redirect("/deploys/project")

class ProjectEditHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, _id):
        url = options.BASE_URL + '/api/v1/deploys/projects/' + _id
        client = AsyncHTTPClient()
        response = yield client.fetch(url)
        if response.body:
            body = json.loads(response.body)
        else:
            body = {}
        self.render("deploys/project/edit.html", items=body)

    @tornado.web.authenticated
    @tornado.web.asynchronous
    @gen.coroutine
    def post(self, _id):
        params = ('project', 'description', 'group')
        item = dict()
        for param in params:
            item[param] = self.get_argument(param, '')
        item['create_by'] = self.get_current_user()
        url = options.BASE_URL + '/api/v1/deploys/projects/' + _id
        request = HTTPRequest(url, method="PUT", body=json.dumps(item))
        client = AsyncHTTPClient()
        response = yield client.fetch(request)
        self.redirect("/deploys/project")

class ProjectDeleteHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self, _id):
        url = options.BASE_URL + '/api/v1/deploys/projects/' + _id
        request = HTTPRequest(url, method="DELETE" )
        client = AsyncHTTPClient()
        response = yield client.fetch(request)
        self.redirect("/deploys/project")

class ProjectDetailHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous

    def get(self, *args, **kwargs):
        self.render("deploys/project/detail.html")

class HostManagementHandler(BaseHandler):
    @tornado.web.asynchronous
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("deploys/project/hostmgmt.html")

class DeployKeyHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self.render("deploys/project/deploy-key.html")

urls = [
    (r"/deploys", DeployHandler),
    (r"/deploys/project", ProjectHandler),
    (r"/deploys/project/add", ProjectAddHandler),
    (r"/deploys/project/edit/(.*)", ProjectEditHandler),
    (r"/deploys/project/del/(.*)", ProjectDeleteHandler),
    (r"/deploys/project/detail/(.*)/hostmgmt", HostManagementHandler),
    (r"/deploys/project/detail/(.*)/deploykey", DeployKeyHandler),
    (r"/deploys/project/detail/(.*)", ProjectDetailHandler),



]