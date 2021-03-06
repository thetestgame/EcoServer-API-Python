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
from ecoserver.api.data_export_api import DataExportApi  # noqa: E501
from ecoserver.rest import ApiException


class TestDataExportApi(unittest.TestCase):
    """DataExportApi unit test stubs"""

    def setUp(self):
        self.api = ecoserver.api.data_export_api.DataExportApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_data_export_get_action_list(self):
        """Test case for data_export_get_action_list

        """
        pass

    def test_data_export_get_environment_list(self):
        """Test case for data_export_get_environment_list

        """
        pass

    def test_data_export_get_export_action(self):
        """Test case for data_export_get_export_action

        """
        pass

    def test_data_export_get_export_environment(self):
        """Test case for data_export_get_export_environment

        """
        pass

    def test_data_export_get_export_species(self):
        """Test case for data_export_get_export_species

        """
        pass

    def test_data_export_get_species_list(self):
        """Test case for data_export_get_species_list

        """
        pass

    def test_data_export_post_export_actions(self):
        """Test case for data_export_post_export_actions

        """
        pass

    def test_data_export_post_export_all(self):
        """Test case for data_export_post_export_all

        """
        pass

    def test_data_export_post_export_chat(self):
        """Test case for data_export_post_export_chat

        """
        pass

    def test_data_export_post_export_environment(self):
        """Test case for data_export_post_export_environment

        """
        pass

    def test_data_export_post_export_species(self):
        """Test case for data_export_post_export_species

        """
        pass


if __name__ == '__main__':
    unittest.main()
