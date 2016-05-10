#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import api.v1.index
import api.v1.deploys.project
import index
import users
from app.apps.deploy import deploy
import api.v1.ansible.ansibletask

urls = api.v1.index.urls \
        + index.urls \
        + users.urls \
        + deploy.urls \
        + api.v1.deploys.project.urls \
        + api.v1.ansible.ansibletask.urls
