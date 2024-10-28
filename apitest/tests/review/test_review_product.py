import logging as logger

import pytest

from apitest.src.helpers.reivew_helper import ReviewHelper
from apitest.src.utilities.genericUtitilies import generate_random_product_review


@pytest.mark.tcid03
def test_create_user():
    logger.info("Test create a new review for products")
    rand_info = generate_random_product_review()
    userId = rand_info['userId']
    productId = rand_info['productId']
    rating = rand_info['rating']
    comment = rand_info['comment']
    logger.info(rand_info)
    #create payload
    payload = {'userId': userId,'productId': productId,'rating':rating, 'comment':comment}
    #make the call
    cust_obj = ReviewHelper()
    cust_api_info = cust_obj.create_reivew(userId=userId, productId=productId, rating=rating, comment=comment)

    assert cust_api_info['userId'] == userId, f"Create reivew api return wrong review. userid: {userId}"
    assert cust_api_info['productId'] == productId, f"Create review api return wrong productId. productId: {productId}"
    assert cust_api_info['rating'] == rating, f"Create review api return wrong rating. rating: {rating}"
    assert cust_api_info['comment'] == comment, f"Create review api return wrong comment. comment: {comment}"

    # import pdb; pdb.set_trace()