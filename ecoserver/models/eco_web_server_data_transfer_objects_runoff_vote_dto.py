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


class EcoWebServerDataTransferObjectsRunoffVoteDTO(object):
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
        'election_id': 'int',
        'voter': 'str',
        'ranked_votes': 'list[int]'
    }

    attribute_map = {
        'election_id': 'electionID',
        'voter': 'voter',
        'ranked_votes': 'rankedVotes'
    }

    def __init__(self, election_id=None, voter=None, ranked_votes=None, _configuration=None):  # noqa: E501
        """EcoWebServerDataTransferObjectsRunoffVoteDTO - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._election_id = None
        self._voter = None
        self._ranked_votes = None
        self.discriminator = None

        if election_id is not None:
            self.election_id = election_id
        if voter is not None:
            self.voter = voter
        if ranked_votes is not None:
            self.ranked_votes = ranked_votes

    @property
    def election_id(self):
        """Gets the election_id of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501


        :return: The election_id of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501
        :rtype: int
        """
        return self._election_id

    @election_id.setter
    def election_id(self, election_id):
        """Sets the election_id of this EcoWebServerDataTransferObjectsRunoffVoteDTO.


        :param election_id: The election_id of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501
        :type: int
        """

        self._election_id = election_id

    @property
    def voter(self):
        """Gets the voter of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501


        :return: The voter of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501
        :rtype: str
        """
        return self._voter

    @voter.setter
    def voter(self, voter):
        """Sets the voter of this EcoWebServerDataTransferObjectsRunoffVoteDTO.


        :param voter: The voter of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501
        :type: str
        """

        self._voter = voter

    @property
    def ranked_votes(self):
        """Gets the ranked_votes of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501


        :return: The ranked_votes of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501
        :rtype: list[int]
        """
        return self._ranked_votes

    @ranked_votes.setter
    def ranked_votes(self, ranked_votes):
        """Sets the ranked_votes of this EcoWebServerDataTransferObjectsRunoffVoteDTO.


        :param ranked_votes: The ranked_votes of this EcoWebServerDataTransferObjectsRunoffVoteDTO.  # noqa: E501
        :type: list[int]
        """

        self._ranked_votes = ranked_votes

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
        if issubclass(EcoWebServerDataTransferObjectsRunoffVoteDTO, dict):
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
        if not isinstance(other, EcoWebServerDataTransferObjectsRunoffVoteDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoWebServerDataTransferObjectsRunoffVoteDTO):
            return True

        return self.to_dict() != other.to_dict()