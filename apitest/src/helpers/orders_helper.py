import jsons

from apitest.src.utilities.RequestsUtility import RequestsUtility


class OrdersHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()
    def create_order(self, json=None, **kwargs):
        # order_data_json = jsons.dumps(json)
        order_data_json = jsons.dumps(json)
        create_order_product =  self.request_utility.post('orders', payload=json, expected_status_code=201)
        return create_order_product

    def verify_status_code(self):
        self.request_utility.status_code
