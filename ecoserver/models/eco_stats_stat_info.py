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


class EcoStatsStatInfo(object):
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
        'has_value_key': 'bool',
        'is_custom': 'bool',
        'is_action': 'bool',
        'is_countable': 'bool',
        'is_aggregatable': 'bool',
        'time_key': 'str'
    }

    attribute_map = {
        'has_value_key': 'hasValueKey',
        'is_custom': 'isCustom',
        'is_action': 'isAction',
        'is_countable': 'isCountable',
        'is_aggregatable': 'isAggregatable',
        'time_key': 'timeKey'
    }

    def __init__(self, has_value_key=None, is_custom=None, is_action=None, is_countable=None, is_aggregatable=None, time_key=None, _configuration=None):  # noqa: E501
        """EcoStatsStatInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._has_value_key = None
        self._is_custom = None
        self._is_action = None
        self._is_countable = None
        self._is_aggregatable = None
        self._time_key = None
        self.discriminator = None

        if has_value_key is not None:
            self.has_value_key = has_value_key
        if is_custom is not None:
            self.is_custom = is_custom
        if is_action is not None:
            self.is_action = is_action
        if is_countable is not None:
            self.is_countable = is_countable
        if is_aggregatable is not None:
            self.is_aggregatable = is_aggregatable
        if time_key is not None:
            self.time_key = time_key

    @property
    def has_value_key(self):
        """Gets the has_value_key of this EcoStatsStatInfo.  # noqa: E501


        :return: The has_value_key of this EcoStatsStatInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_value_key

    @has_value_key.setter
    def has_value_key(self, has_value_key):
        """Sets the has_value_key of this EcoStatsStatInfo.


        :param has_value_key: The has_value_key of this EcoStatsStatInfo.  # noqa: E501
        :type: bool
        """

        self._has_value_key = has_value_key

    @property
    def is_custom(self):
        """Gets the is_custom of this EcoStatsStatInfo.  # noqa: E501


        :return: The is_custom of this EcoStatsStatInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom

    @is_custom.setter
    def is_custom(self, is_custom):
        """Sets the is_custom of this EcoStatsStatInfo.


        :param is_custom: The is_custom of this EcoStatsStatInfo.  # noqa: E501
        :type: bool
        """

        self._is_custom = is_custom

    @property
    def is_action(self):
        """Gets the is_action of this EcoStatsStatInfo.  # noqa: E501


        :return: The is_action of this EcoStatsStatInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_action

    @is_action.setter
    def is_action(self, is_action):
        """Sets the is_action of this EcoStatsStatInfo.


        :param is_action: The is_action of this EcoStatsStatInfo.  # noqa: E501
        :type: bool
        """

        self._is_action = is_action

    @property
    def is_countable(self):
        """Gets the is_countable of this EcoStatsStatInfo.  # noqa: E501


        :return: The is_countable of this EcoStatsStatInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_countable

    @is_countable.setter
    def is_countable(self, is_countable):
        """Sets the is_countable of this EcoStatsStatInfo.


        :param is_countable: The is_countable of this EcoStatsStatInfo.  # noqa: E501
        :type: bool
        """

        self._is_countable = is_countable

    @property
    def is_aggregatable(self):
        """Gets the is_aggregatable of this EcoStatsStatInfo.  # noqa: E501


        :return: The is_aggregatable of this EcoStatsStatInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_aggregatable

    @is_aggregatable.setter
    def is_aggregatable(self, is_aggregatable):
        """Sets the is_aggregatable of this EcoStatsStatInfo.


        :param is_aggregatable: The is_aggregatable of this EcoStatsStatInfo.  # noqa: E501
        :type: bool
        """

        self._is_aggregatable = is_aggregatable

    @property
    def time_key(self):
        """Gets the time_key of this EcoStatsStatInfo.  # noqa: E501


        :return: The time_key of this EcoStatsStatInfo.  # noqa: E501
        :rtype: str
        """
        return self._time_key

    @time_key.setter
    def time_key(self, time_key):
        """Sets the time_key of this EcoStatsStatInfo.


        :param time_key: The time_key of this EcoStatsStatInfo.  # noqa: E501
        :type: str
        """

        self._time_key = time_key

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
        if issubclass(EcoStatsStatInfo, dict):
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
        if not isinstance(other, EcoStatsStatInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoStatsStatInfo):
            return True

        return self.to_dict() != other.to_dict()
