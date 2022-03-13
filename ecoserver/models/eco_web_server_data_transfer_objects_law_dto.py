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


class EcoWebServerDataTransferObjectsLawDTO(object):
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
        'id': 'int',
        'name': 'str',
        'user_description': 'str',
        'state': 'str',
        'creator': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'user_description': 'userDescription',
        'state': 'state',
        'creator': 'creator',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, user_description=None, state=None, creator=None, description=None, _configuration=None):  # noqa: E501
        """EcoWebServerDataTransferObjectsLawDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._user_description = None
        self._state = None
        self._creator = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if user_description is not None:
            self.user_description = user_description
        if state is not None:
            self.state = state
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501


        :return: The id of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcoWebServerDataTransferObjectsLawDTO.


        :param id: The id of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501


        :return: The name of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EcoWebServerDataTransferObjectsLawDTO.


        :param name: The name of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def user_description(self):
        """Gets the user_description of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501


        :return: The user_description of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :rtype: str
        """
        return self._user_description

    @user_description.setter
    def user_description(self, user_description):
        """Sets the user_description of this EcoWebServerDataTransferObjectsLawDTO.


        :param user_description: The user_description of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :type: str
        """

        self._user_description = user_description

    @property
    def state(self):
        """Gets the state of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501


        :return: The state of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EcoWebServerDataTransferObjectsLawDTO.


        :param state: The state of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def creator(self):
        """Gets the creator of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501


        :return: The creator of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this EcoWebServerDataTransferObjectsLawDTO.


        :param creator: The creator of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def description(self):
        """Gets the description of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501


        :return: The description of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EcoWebServerDataTransferObjectsLawDTO.


        :param description: The description of this EcoWebServerDataTransferObjectsLawDTO.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(EcoWebServerDataTransferObjectsLawDTO, dict):
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
        if not isinstance(other, EcoWebServerDataTransferObjectsLawDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoWebServerDataTransferObjectsLawDTO):
            return True

        return self.to_dict() != other.to_dict()