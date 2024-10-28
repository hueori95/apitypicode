from apitest.src.utilities.RequestsUtility import RequestsUtility


class ProductHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()
    def find_products(self, payload = None, params=None, header = None, **kwargs):
        if not params:
            params = {"name": "Samsung Galaxy S21"}
        # dict() same List và Tuple
        search_products =  self.request_utility.get('products',payload=None, params=params, headers=header, expected_status_code=200)
        return search_products
