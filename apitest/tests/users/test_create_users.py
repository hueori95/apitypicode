import logging as logger

import pytest

from apitest.src.helpers.user_helper import UserHelper
from apitest.src.utilities.genericUtitilies import generate_random_email_username_and_password


@pytest.mark.tcid01
def test_create_user():
    logger.info("Test create a new users with username, email and password: ")
    rand_info = generate_random_email_username_and_password()
    email = rand_info['email']
    password = rand_info['password']
    username = rand_info['username']
    logger.info(rand_info)
    #create payload
    payload = {'username': username,'email': email,'password':password}
    #make the call
    cust_obj = UserHelper()
    cust_api_info = cust_obj.create_users(email=email, password=password, username=username)

    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['username'] == username, f"Create customer api return wrong email. username: {username}"

    # import pdb; pdb.set_trace()