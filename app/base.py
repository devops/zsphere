#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import tornado.web
import hashlib


class BaseHandler(tornado.web.RequestHandler):
    """ """

    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        return self.get_secure_cookie("username")

    def write_error(self, status_code, **kwargs):
        self.render('error.html', status=self._status_code)

    def data_received(self, chunk):
        pass


class ErrorHandler(tornado.web.ErrorHandler):
    def prepare(self):
        self.render('error.html', status=self._status_code)


def generate_password(password, method='md5'):
    m = hashlib.new(method, password).hexdigest()
    return m
