#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import json
from bson import ObjectId
from bson import json_util
from tornado import gen
from app.api.v1.base import APIHandler, authenticated


class ProjectsHandler(APIHandler):
    #@authenticated
    @gen.coroutine
    def get(self, *args, **kwargs):
        """获取全部项目列表，支持参数查询
        参数：
            key 查询key
            value 查询value
        用法:
            api/v1/delopys/projects?key=foo&value=foo
        """

        doc = []
        if len(self.request.arguments) > 1:
            key = self.get_argument("key", "")
            value = self.get_argument("value", "")
            finder = {key: {"$regex": value}}
        else:
            finder = {}
        cursor = self.db.project.find(finder)
        for d in (yield cursor.to_list(length=None)):
            doc.append(d)
        self.write(json.dumps(doc, default=json_util.default))

    @gen.coroutine
    def post(self, *args, **kwargs):
        """添加一个新的项目信息"""

        project_data = json.loads(self.request.body)
        project_id = yield self.db.project.insert(project_data)
        response = yield self.db.project.find_one(ObjectId(project_id))
        self.write(json.dumps(response, default=json_util.default))
        self.set_status(201)


class ProjectHandler(APIHandler):
    @gen.coroutine
    #@authenticated
    def get(self, _id):
        """通过ID获取一个项目信息"""
        response = yield self.db.project.find_one(ObjectId(_id))
        self.write(json.dumps(response, default=json_util.default))


    @gen.coroutine
    def put(self, _id):
        """通过ID更新一个项目信息"""
        project_data = json.loads(self.request.body)
        yield self.db.project.update({'_id': ObjectId(_id)}, {"$set": project_data})
        response = yield self.db.project.find_one(ObjectId(_id))
        self.write(json.dumps(response, default=json_util.default))
        self.set_status(201)

    @gen.coroutine
    def delete(self, _id):
        """通过ID删除一个项目信息"""
        yield self.db.project.remove({"_id": ObjectId(_id)})
        self.set_status(204)


urls = [
    (r"/api/v1/deploys/projects", ProjectsHandler),
    (r"/api/v1/deploys/projects/([a-f0-9]+)", ProjectHandler),
]
