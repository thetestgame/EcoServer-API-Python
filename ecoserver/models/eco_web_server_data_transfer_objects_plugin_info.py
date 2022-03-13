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


class EcoWebServerDataTransferObjectsPluginInfo(object):
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
        'type_name': 'str',
        'status': 'str',
        'has_config': 'bool'
    }

    attribute_map = {
        'type_name': 'typeName',
        'status': 'status',
        'has_config': 'hasConfig'
    }

    def __init__(self, type_name=None, status=None, has_config=None, _configuration=None):  # noqa: E501
        """EcoWebServerDataTransferObjectsPluginInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._type_name = None
        self._status = None
        self._has_config = None
        self.discriminator = None

        if type_name is not None:
            self.type_name = type_name
        if status is not None:
            self.status = status
        if has_config is not None:
            self.has_config = has_config

    @property
    def type_name(self):
        """Gets the type_name of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501


        :return: The type_name of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this EcoWebServerDataTransferObjectsPluginInfo.


        :param type_name: The type_name of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def status(self):
        """Gets the status of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501


        :return: The status of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EcoWebServerDataTransferObjectsPluginInfo.


        :param status: The status of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def has_config(self):
        """Gets the has_config of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501


        :return: The has_config of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_config

    @has_config.setter
    def has_config(self, has_config):
        """Sets the has_config of this EcoWebServerDataTransferObjectsPluginInfo.


        :param has_config: The has_config of this EcoWebServerDataTransferObjectsPluginInfo.  # noqa: E501
        :type: bool
        """

        self._has_config = has_config

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
        if issubclass(EcoWebServerDataTransferObjectsPluginInfo, dict):
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
        if not isinstance(other, EcoWebServerDataTransferObjectsPluginInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoWebServerDataTransferObjectsPluginInfo):
            return True

        return self.to_dict() != other.to_dict()
