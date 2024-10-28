import logging as logger

import jsons
import pytest

from apitest.src.helpers.product_helper import ProductHelper
from apitest.src.helpers.user_helper import UserHelper
from apitest.src.utilities.genericUtitilies import generate_random_email_username_and_password


@pytest.mark.tcid02
def test_search_product():
    logger.info("Test search product with name = iPhone 13 ")
    params = {"name":"iPhone 13"}
    #make the call
    cust_obj = ProductHelper()
    cust_api_info = cust_obj.find_products(params=params)
    logger.debug(cust_api_info)
    data_info = jsons.load(cust_api_info)

    for data in data_info:
        logger.info(data["name"])
        assert data["name"] == "iPhone 13", f"not correctly"
    # import pdb; pdb.set_trace()
