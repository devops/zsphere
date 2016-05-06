#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

PORT = "8000"
DEBUG = "True"
SECRET = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="

MONGO_HOST = "127.0.0.1"
MONGO_PORT = 27017
MONGO_NAME = "zsphere"
MONGO_USER = "zsphere"
MONGO_PASSWORD = "zsphere"
MONGO_URI = "mongodb://%s:%s@%s:%d/%s" % (MONGO_USER, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_NAME)


BASE_URL = "http://127.0.0.1:8000"