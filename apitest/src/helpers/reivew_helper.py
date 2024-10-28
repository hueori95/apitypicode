from apitest.src.utilities.RequestsUtility import RequestsUtility
from apitest.src.utilities.genericUtitilies import generate_random_product_review


class ReviewHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()
    def create_reivew(self, userId=None, productId=None, rating=None, comment=None, **kwargs):

        # dict() same List và Tuple
        payload = dict()
        payload['userId'] = userId
        payload['productId'] = productId
        payload['rating'] = rating
        payload['comment'] = comment
        payload.update(kwargs)
        create_review =  self.request_utility.post('reviews',payload=payload, expected_status_code=201)
        return create_review

    def verify_status_code(self):
        self.request_utility.status_code
