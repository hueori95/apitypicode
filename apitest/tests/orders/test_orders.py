import json
import logging as logger

import pytest

from apitest.src.helpers.orders_helper import OrdersHelper
from apitest.src.utilities.genericUtitilies import generate_random_email_username_and_password


@pytest.mark.tcid04
def test_orders():
    logger.info("Test orders products: ")
    order_data = {
        "id": "2",
        "userId": 2,
        "status": "processing",
        "items": [
            {
                "productId": 3,
                "quantity": 2
            },
            {
                "productId": 1,
                "quantity": 1
            }
        ]
    }


    # import pdb; pdb.set_trace()
    #make the call
    cust_obj = OrdersHelper()
    cust_api_info = cust_obj.create_order(json=order_data)
    assert order_data == cust_api_info , f"Create order api wrong"
    # import pdb; pdb.set_trace()