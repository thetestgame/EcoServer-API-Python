# coding: utf-8

"""
    Eco Game API

    First API draft for Eco. Heavy work in progress and subject to changes.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ecoserver
from ecoserver.api.users_api import UsersApi  # noqa: E501
from ecoserver.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = ecoserver.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_get_users(self):
        """Test case for users_get_users

        """
        pass


if __name__ == '__main__':
    unittest.main()
