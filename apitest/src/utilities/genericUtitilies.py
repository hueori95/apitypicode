import logging as logger
import random
import string


def generate_random_email_username_and_password(domain=None, email_prefix=None):
    logger.info("Generating random email and password.")
    if not domain:
        domain = "example.com"
    if not email_prefix:
        email_prefix = "testuser"

    random_email_string_length = 10
    random_string = ''.join(random.choices(string.ascii_lowercase, k = random_email_string_length))
    email = email_prefix + '_' + random_string + '@' + domain
    password_length = 20
    password_string = ''.join(random.choices(string.ascii_lowercase, k = password_length))
    username_lengh = 10
    username_string = ''.join(random.choices(string.ascii_lowercase, k = username_lengh))

    random_info = {'email': email, 'password': password_string, 'username': username_string}
    logger.info(f"Randomly generated email and password: {random_info}")

    return random_info

def generate_random_product_review():
    logger.info("Generating random product and review")

    userId_length = 10
    userid = ''.join(random.choices(string.ascii_lowercase, k = userId_length))

    productId_length = 10
    productId = ''.join(random.choices(string.ascii_lowercase, k=productId_length))

    rating_length = 1
    rating = ''.join(random.choices(string.digits, k = rating_length))

    comment = userid + ' comments: The product is very good'

    random_info = {'userId': userid, 'productId': productId,'rating':rating, 'comment': comment}
    logger.info(f"Randomly generated email and password: {random_info}")

    return random_info