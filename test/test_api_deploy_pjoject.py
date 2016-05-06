#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import unittest
import json
import requests
import tornado.testing
from tornado.testing import AsyncTestCase
from tornado.httpclient import AsyncHTTPClient, HTTPRequest

projects_url = 'http://127.0.0.1:8000/api/v1/deploys/projects'
project_data = {"project": "openstack", "description": "deploys openstak", "group": "production"}

# 添加测试数据
r = requests.post(projects_url, data=json.dumps(project_data))
project_id = r.json()['_id']['$oid']


class ProjectsTestCase(AsyncTestCase):

    def setUp(self):
        AsyncTestCase.setUp(self)
        self.url = projects_url
        self.data = project_data

    @tornado.testing.gen_test
    def test_projects_get(self):
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(self.url)
        print response.body

    @tornado.testing.gen_test
    def test_projects_post(self):
        request = HTTPRequest(self.url, method="POST", body=json.dumps(self.data))
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(request)
        print response.body
        # 清理数据
        res_id = json.loads(response.body)['_id']['$oid']
        requests.delete(self.url + '/' + res_id)


class ProjectTestCase(AsyncTestCase):

    def setUp(self):
        AsyncTestCase.setUp(self)
        self.url = projects_url
        self.data = project_data
        self.project_id = project_id

    @tornado.testing.gen_test
    def test_project_aget(self):
        url = self.url + '/' + self.project_id
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(url)
        print response.body

    @tornado.testing.gen_test
    def test_project_bput(self):
        url = self.url + '/' + self.project_id
        request = HTTPRequest(url, method="PUT", body=json.dumps(self.data))
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(request)
        print response.body

    @tornado.testing.gen_test
    def test_project_cdelete(self):
        url = self.url + '/' + self.project_id
        request = HTTPRequest(url, method="DELETE")
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(request)
        print response.body


if __name__ == '__main__':
    unittest.main()
