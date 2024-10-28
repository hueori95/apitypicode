import requests
from apitest.src.config.hosts_config import API_HOSTS
import jsons
import logging as logger
import os

class RequestsUtility(object):

    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

    def post(self, enpoint, payload=None,json=None, headers=None, expected_status_code = 201):
        if not headers:
            headers = {"Content-Type":"application/json"}
        url = self.base_url + enpoint
        rs_api = requests.post(url, data=jsons.dumps(payload), json=json, headers=headers)
        # import pdb; pdb.set_trace()
        self.status_code = rs_api.status_code
        self.rs_json = rs_api.json()
        return rs_api.json()

    def assert_status_code(self):
        assert  self.status_code == self.expected_status_code, (f"Bad status code. "
                                                                f"expected {self.expected_status_code}"
                                                                f"Actual status code: {self.status_code}")
    def get(self, enpoint, payload=None, params=None, headers=None, expected_status_code = 200):
        if not headers:
            headers = {"Content-Type":"application/json"}

        self.url = self.base_url + enpoint
        rs_api = requests.get(self.url, data=jsons.dumps(payload),params=params, headers=headers)
        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()
        self.assert_status_code()

        logger.debug(f"GET API | response: {self.rs_json}")

        return self.rs_json

