# coding: utf-8

"""
    Eco Game API

    First API draft for Eco. Heavy work in progress and subject to changes.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ecoserver.configuration import Configuration


class EcoWebServerWebModelsAdminReturnModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action': 'EcoWebServerWebModelsAction',
        'message': 'str'
    }

    attribute_map = {
        'action': 'action',
        'message': 'message'
    }

    def __init__(self, action=None, message=None, _configuration=None):  # noqa: E501
        """EcoWebServerWebModelsAdminReturnModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action = None
        self._message = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if message is not None:
            self.message = message

    @property
    def action(self):
        """Gets the action of this EcoWebServerWebModelsAdminReturnModel.  # noqa: E501


        :return: The action of this EcoWebServerWebModelsAdminReturnModel.  # noqa: E501
        :rtype: EcoWebServerWebModelsAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this EcoWebServerWebModelsAdminReturnModel.


        :param action: The action of this EcoWebServerWebModelsAdminReturnModel.  # noqa: E501
        :type: EcoWebServerWebModelsAction
        """

        self._action = action

    @property
    def message(self):
        """Gets the message of this EcoWebServerWebModelsAdminReturnModel.  # noqa: E501


        :return: The message of this EcoWebServerWebModelsAdminReturnModel.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this EcoWebServerWebModelsAdminReturnModel.


        :param message: The message of this EcoWebServerWebModelsAdminReturnModel.  # noqa: E501
        :type: str
        """

        self._message = message

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EcoWebServerWebModelsAdminReturnModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EcoWebServerWebModelsAdminReturnModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoWebServerWebModelsAdminReturnModel):
            return True

        return self.to_dict() != other.to_dict()