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


class EcoWebServerDataTransferObjectsChatMessageDTO(object):
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
        'timestamp': 'float',
        'sender': 'str',
        'receiver': 'str',
        'text': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'sender': 'sender',
        'receiver': 'receiver',
        'text': 'text'
    }

    def __init__(self, timestamp=None, sender=None, receiver=None, text=None, _configuration=None):  # noqa: E501
        """EcoWebServerDataTransferObjectsChatMessageDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._timestamp = None
        self._sender = None
        self._receiver = None
        self._text = None
        self.discriminator = None

        if timestamp is not None:
            self.timestamp = timestamp
        if sender is not None:
            self.sender = sender
        if receiver is not None:
            self.receiver = receiver
        if text is not None:
            self.text = text

    @property
    def timestamp(self):
        """Gets the timestamp of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501


        :return: The timestamp of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this EcoWebServerDataTransferObjectsChatMessageDTO.


        :param timestamp: The timestamp of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def sender(self):
        """Gets the sender of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501


        :return: The sender of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this EcoWebServerDataTransferObjectsChatMessageDTO.


        :param sender: The sender of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def receiver(self):
        """Gets the receiver of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501


        :return: The receiver of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this EcoWebServerDataTransferObjectsChatMessageDTO.


        :param receiver: The receiver of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def text(self):
        """Gets the text of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501


        :return: The text of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this EcoWebServerDataTransferObjectsChatMessageDTO.


        :param text: The text of this EcoWebServerDataTransferObjectsChatMessageDTO.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(EcoWebServerDataTransferObjectsChatMessageDTO, dict):
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
        if not isinstance(other, EcoWebServerDataTransferObjectsChatMessageDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoWebServerDataTransferObjectsChatMessageDTO):
            return True

        return self.to_dict() != other.to_dict()
