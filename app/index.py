#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

from tornado import web
from base import BaseHandler


class IndexHandler(BaseHandler):
    @web.authenticated
    def get(self):
        self.render("index.html")

urls = [
    (r"/", IndexHandler),
]
