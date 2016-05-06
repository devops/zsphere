#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import tornado.web
from tornado import gen

from base import BaseHandler, generate_password


class UsersLoginHandler(BaseHandler):
    def get(self):
        self.render('users/login.html', msg=None)

    @tornado.web.asynchronous
    @gen.coroutine
    def post(self):
        self.set_secure_cookie("username", self.get_argument("username"))
        user = self.get_argument("username").encode("UTF-8")
        pwd = self.get_argument("password").encode("UTF-8")
        finder = {"$and": [{"username": user}, {"password": generate_password(pwd)}]}
        response = yield self.db.users.find_one(finder)

        if response:
            self.redirect("/")
        else:
            self.render("users/login.html", msg=r"用户名或密码错误")


class UsersLogoutHandler(BaseHandler):
    def get(self):
        # if self.get_argument("logout", None):
        #     self.clear_cookie("username")
        #     self.redirect("/login")
        self.clear_cookie("username")
        self.render("users/login.html", msg=r"您已退出，请重新登陆")


class UsersSignupHandler(BaseHandler):
    """docstring for ServerAddHandler"""

    def get(self):
        self.render("users/signup.html")

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        params = ('username', 'password', 'phone', )
        item = dict()
        for param in params:
            item[param] = self.get_argument(param, '')

        yield gen.Task(self.db.users.insert, item)
        for i in item:
            print(i)
        self.redirect("/login", user=item["username"])

urls = [
    (r"/users/login", UsersLoginHandler),
    (r"/users/logout", UsersLogoutHandler),
    (r"/users/signup", UsersSignupHandler),
]