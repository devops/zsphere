#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import json
from bson import json_util
from ansible.runner import Runner
from ansible.playbook import PlayBook
from ansible import callbacks
from ansible import utils

from app.api.v1.base import APIHandler

class AdhocJobs(object):
    def __init__(self, host_list=None,
                 module_name=None,
                 module_args=None,
                 pattern=None,
                 forks=10,
                 private_key_file=None
                 ):
        self.host_list = host_list
        self.module_name = module_name
        self.module_args = module_args
        self.pattern = pattern
        self.forks = forks
        self.private_key_file = private_key_file

    def run(self):
        runner = Runner(
            host_list = self.host_list,
            module_name = self.module_name,
            module_args = self.module_args,
            pattern = self.pattern,
            forks = self.forks
        )
        datastructure = runner.run()
        if len(datastructure['dark']) == 0 and len(datastructure['contacted']) == 0:
            results = {"error": "No hosts found"}
        else:
            results = datastructure
        return results


class AdhocJobsHandler(APIHandler):
    def get(self):
        pass


    def post(self):
        job_data = json.loads(self.request.body)

        job = AdhocJobs(job_data['hostlist'],
                        job_data['modulename'],
                        job_data['moduleargs'],
                        job_data['pattern']
                        )

        job_result = job.run()
        self.write(json.dumps(job_result, default=json_util.default))


class PlaybookJobs(object):
    """

    """
    def __init__(self, playbook=None, host_list=None, module_path=None):
        self.playbook = playbook
        self.host_list = host_list
        self.module_path = module_path
        self.stats = callbacks.AggregateStats()
        self.playbook_cb = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
        self.runner_cb = callbacks.PlaybookRunnerCallbacks(self.stats, verbose=utils.VERBOSITY)

    def run(self):
        pb = PlayBook(playbook=self.playbook,
                      host_list=self.host_list,
                      module_path=self.module_path,
                      callbacks=self.playbook_cb,
                      runner_callbacks=self.runner_cb,
                      stats=self.stats
                      )
        results = pb.run()
        return results
        print results

class PlaybookJobsHandler(APIHandler):
    def get(self, *args, **kwargs):
       pass

    def post(self, *args, **kwargs):
        job_data = json.loads(self.request.body)
        job = PlaybookJobs(job_data['playbook'],
                        job_data['host_list'],
                        job_data['module_path']
                        )

        job_result = job.run()
        self.write(json.dumps(job_result, default=json_util.default))

urls = [
    (r"/api/v1/ansible/adhocjobs", AdhocJobsHandler),
    (r"/api/v1/ansible/playbookjobs", PlaybookJobsHandler)
]