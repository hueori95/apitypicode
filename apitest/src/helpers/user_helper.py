from apitest.src.utilities.RequestsUtility import RequestsUtility
from apitest.src.utilities.genericUtitilies import generate_random_email_username_and_password


class UserHelper(object):

    def __init__(self):
        self.request_utility = RequestsUtility()
    def create_users(self, email=None, password=None, username=None, **kwargs):
        if not email:
            ep = generate_random_email_username_and_password()
            email = ep['email']
        if not password:
            password = 'password'
        if not username:
            username = 'username'

        # dict() same List và Tuple
        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload['username'] = username
        payload.update(kwargs)
        create_user_json =  self.request_utility.post('users',payload=payload, expected_status_code=201)
        return create_user_json

    def verify_status_code(self):
        self.request_utility.status_code
