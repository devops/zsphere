#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import unittest
import json


import tornado.testing
from tornado.testing import AsyncTestCase
from tornado.httpclient import AsyncHTTPClient, HTTPRequest


class AdhocJobsTestCase(AsyncTestCase):
    @tornado.testing.gen_test
    def test_AdhocJobs_post(self):
        url = "http://127.0.0.1:8000/api/v1/ansible/adhocjobs"
        test_data = {"hostlist" : "/Users/z/work/pac/ansible-roles/hosts",
                     "modulename": "ping",
                     "moduleargs": "",
                     "pattern": "all"
                     }
        request = HTTPRequest(url, method="POST",body=json.dumps(test_data))
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(request)
        print response.body

class PlaybookJobsTestCase(AsyncTestCase):
    @tornado.testing.gen_test
    def test_PlaybookJobs_post(self):
        url = "http://127.0.0.1:8000/api/v1/ansible/playbookjobs"
        test_data = {"playbook": "/Users/z/work/pac/ansible-roles/test.yml",
                     "host_list" : "/Users/z/work/pac/ansible-roles/hosts",
                     "module_path": ""
                     }
        request = HTTPRequest(url, method="POST",body=json.dumps(test_data))
        client = AsyncHTTPClient(self.io_loop)
        response = yield client.fetch(request)
        print response.body

if __name__ == '__main__':
    unittest.main()