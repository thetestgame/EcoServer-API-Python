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


class EcoSharedMathVector3i(object):
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
        'x': 'int',
        'y': 'int',
        'z': 'int',
        'magnitude': 'float',
        'sqr_magnitude': 'int',
        'mult_together': 'int',
        'xz': 'EcoSharedMathVector2i',
        'xz_full_neighbors_and_self': 'list[EcoSharedMathVector3i]',
        'xz_neighbors_and_self': 'list[EcoSharedMathVector3i]',
        'xz_neighbors_and_dir': 'list[EcoSharedMathRay]',
        'xz_neighbors': 'list[EcoSharedMathVector3i]',
        'xz_full_neighbors': 'list[EcoSharedMathVector3i]',
        'xyz_neighbors_and_self': 'list[EcoSharedMathVector3i]',
        'xyz_neighbors': 'list[EcoSharedMathVector3i]',
        'full26_neighbors': 'list[EcoSharedMathVector3i]',
        'normalized': 'SystemNumericsVector3',
        'normalized_or_zero': 'SystemNumericsVector3'
    }

    attribute_map = {
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'magnitude': 'magnitude',
        'sqr_magnitude': 'sqrMagnitude',
        'mult_together': 'multTogether',
        'xz': 'xz',
        'xz_full_neighbors_and_self': 'xzFullNeighborsAndSelf',
        'xz_neighbors_and_self': 'xzNeighborsAndSelf',
        'xz_neighbors_and_dir': 'xzNeighborsAndDir',
        'xz_neighbors': 'xzNeighbors',
        'xz_full_neighbors': 'xzFullNeighbors',
        'xyz_neighbors_and_self': 'xyzNeighborsAndSelf',
        'xyz_neighbors': 'xyzNeighbors',
        'full26_neighbors': 'full26Neighbors',
        'normalized': 'normalized',
        'normalized_or_zero': 'normalizedOrZero'
    }

    def __init__(self, x=None, y=None, z=None, magnitude=None, sqr_magnitude=None, mult_together=None, xz=None, xz_full_neighbors_and_self=None, xz_neighbors_and_self=None, xz_neighbors_and_dir=None, xz_neighbors=None, xz_full_neighbors=None, xyz_neighbors_and_self=None, xyz_neighbors=None, full26_neighbors=None, normalized=None, normalized_or_zero=None, _configuration=None):  # noqa: E501
        """EcoSharedMathVector3i - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._x = None
        self._y = None
        self._z = None
        self._magnitude = None
        self._sqr_magnitude = None
        self._mult_together = None
        self._xz = None
        self._xz_full_neighbors_and_self = None
        self._xz_neighbors_and_self = None
        self._xz_neighbors_and_dir = None
        self._xz_neighbors = None
        self._xz_full_neighbors = None
        self._xyz_neighbors_and_self = None
        self._xyz_neighbors = None
        self._full26_neighbors = None
        self._normalized = None
        self._normalized_or_zero = None
        self.discriminator = None

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if magnitude is not None:
            self.magnitude = magnitude
        if sqr_magnitude is not None:
            self.sqr_magnitude = sqr_magnitude
        if mult_together is not None:
            self.mult_together = mult_together
        if xz is not None:
            self.xz = xz
        if xz_full_neighbors_and_self is not None:
            self.xz_full_neighbors_and_self = xz_full_neighbors_and_self
        if xz_neighbors_and_self is not None:
            self.xz_neighbors_and_self = xz_neighbors_and_self
        if xz_neighbors_and_dir is not None:
            self.xz_neighbors_and_dir = xz_neighbors_and_dir
        if xz_neighbors is not None:
            self.xz_neighbors = xz_neighbors
        if xz_full_neighbors is not None:
            self.xz_full_neighbors = xz_full_neighbors
        if xyz_neighbors_and_self is not None:
            self.xyz_neighbors_and_self = xyz_neighbors_and_self
        if xyz_neighbors is not None:
            self.xyz_neighbors = xyz_neighbors
        if full26_neighbors is not None:
            self.full26_neighbors = full26_neighbors
        if normalized is not None:
            self.normalized = normalized
        if normalized_or_zero is not None:
            self.normalized_or_zero = normalized_or_zero

    @property
    def x(self):
        """Gets the x of this EcoSharedMathVector3i.  # noqa: E501


        :return: The x of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this EcoSharedMathVector3i.


        :param x: The x of this EcoSharedMathVector3i.  # noqa: E501
        :type: int
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this EcoSharedMathVector3i.  # noqa: E501


        :return: The y of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this EcoSharedMathVector3i.


        :param y: The y of this EcoSharedMathVector3i.  # noqa: E501
        :type: int
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this EcoSharedMathVector3i.  # noqa: E501


        :return: The z of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: int
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this EcoSharedMathVector3i.


        :param z: The z of this EcoSharedMathVector3i.  # noqa: E501
        :type: int
        """

        self._z = z

    @property
    def magnitude(self):
        """Gets the magnitude of this EcoSharedMathVector3i.  # noqa: E501


        :return: The magnitude of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: float
        """
        return self._magnitude

    @magnitude.setter
    def magnitude(self, magnitude):
        """Sets the magnitude of this EcoSharedMathVector3i.


        :param magnitude: The magnitude of this EcoSharedMathVector3i.  # noqa: E501
        :type: float
        """

        self._magnitude = magnitude

    @property
    def sqr_magnitude(self):
        """Gets the sqr_magnitude of this EcoSharedMathVector3i.  # noqa: E501


        :return: The sqr_magnitude of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: int
        """
        return self._sqr_magnitude

    @sqr_magnitude.setter
    def sqr_magnitude(self, sqr_magnitude):
        """Sets the sqr_magnitude of this EcoSharedMathVector3i.


        :param sqr_magnitude: The sqr_magnitude of this EcoSharedMathVector3i.  # noqa: E501
        :type: int
        """

        self._sqr_magnitude = sqr_magnitude

    @property
    def mult_together(self):
        """Gets the mult_together of this EcoSharedMathVector3i.  # noqa: E501


        :return: The mult_together of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: int
        """
        return self._mult_together

    @mult_together.setter
    def mult_together(self, mult_together):
        """Sets the mult_together of this EcoSharedMathVector3i.


        :param mult_together: The mult_together of this EcoSharedMathVector3i.  # noqa: E501
        :type: int
        """

        self._mult_together = mult_together

    @property
    def xz(self):
        """Gets the xz of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xz of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: EcoSharedMathVector2i
        """
        return self._xz

    @xz.setter
    def xz(self, xz):
        """Sets the xz of this EcoSharedMathVector3i.


        :param xz: The xz of this EcoSharedMathVector3i.  # noqa: E501
        :type: EcoSharedMathVector2i
        """

        self._xz = xz

    @property
    def xz_full_neighbors_and_self(self):
        """Gets the xz_full_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xz_full_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._xz_full_neighbors_and_self

    @xz_full_neighbors_and_self.setter
    def xz_full_neighbors_and_self(self, xz_full_neighbors_and_self):
        """Sets the xz_full_neighbors_and_self of this EcoSharedMathVector3i.


        :param xz_full_neighbors_and_self: The xz_full_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._xz_full_neighbors_and_self = xz_full_neighbors_and_self

    @property
    def xz_neighbors_and_self(self):
        """Gets the xz_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xz_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._xz_neighbors_and_self

    @xz_neighbors_and_self.setter
    def xz_neighbors_and_self(self, xz_neighbors_and_self):
        """Sets the xz_neighbors_and_self of this EcoSharedMathVector3i.


        :param xz_neighbors_and_self: The xz_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._xz_neighbors_and_self = xz_neighbors_and_self

    @property
    def xz_neighbors_and_dir(self):
        """Gets the xz_neighbors_and_dir of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xz_neighbors_and_dir of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathRay]
        """
        return self._xz_neighbors_and_dir

    @xz_neighbors_and_dir.setter
    def xz_neighbors_and_dir(self, xz_neighbors_and_dir):
        """Sets the xz_neighbors_and_dir of this EcoSharedMathVector3i.


        :param xz_neighbors_and_dir: The xz_neighbors_and_dir of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathRay]
        """

        self._xz_neighbors_and_dir = xz_neighbors_and_dir

    @property
    def xz_neighbors(self):
        """Gets the xz_neighbors of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xz_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._xz_neighbors

    @xz_neighbors.setter
    def xz_neighbors(self, xz_neighbors):
        """Sets the xz_neighbors of this EcoSharedMathVector3i.


        :param xz_neighbors: The xz_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._xz_neighbors = xz_neighbors

    @property
    def xz_full_neighbors(self):
        """Gets the xz_full_neighbors of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xz_full_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._xz_full_neighbors

    @xz_full_neighbors.setter
    def xz_full_neighbors(self, xz_full_neighbors):
        """Sets the xz_full_neighbors of this EcoSharedMathVector3i.


        :param xz_full_neighbors: The xz_full_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._xz_full_neighbors = xz_full_neighbors

    @property
    def xyz_neighbors_and_self(self):
        """Gets the xyz_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xyz_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._xyz_neighbors_and_self

    @xyz_neighbors_and_self.setter
    def xyz_neighbors_and_self(self, xyz_neighbors_and_self):
        """Sets the xyz_neighbors_and_self of this EcoSharedMathVector3i.


        :param xyz_neighbors_and_self: The xyz_neighbors_and_self of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._xyz_neighbors_and_self = xyz_neighbors_and_self

    @property
    def xyz_neighbors(self):
        """Gets the xyz_neighbors of this EcoSharedMathVector3i.  # noqa: E501


        :return: The xyz_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._xyz_neighbors

    @xyz_neighbors.setter
    def xyz_neighbors(self, xyz_neighbors):
        """Sets the xyz_neighbors of this EcoSharedMathVector3i.


        :param xyz_neighbors: The xyz_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._xyz_neighbors = xyz_neighbors

    @property
    def full26_neighbors(self):
        """Gets the full26_neighbors of this EcoSharedMathVector3i.  # noqa: E501


        :return: The full26_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: list[EcoSharedMathVector3i]
        """
        return self._full26_neighbors

    @full26_neighbors.setter
    def full26_neighbors(self, full26_neighbors):
        """Sets the full26_neighbors of this EcoSharedMathVector3i.


        :param full26_neighbors: The full26_neighbors of this EcoSharedMathVector3i.  # noqa: E501
        :type: list[EcoSharedMathVector3i]
        """

        self._full26_neighbors = full26_neighbors

    @property
    def normalized(self):
        """Gets the normalized of this EcoSharedMathVector3i.  # noqa: E501


        :return: The normalized of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: SystemNumericsVector3
        """
        return self._normalized

    @normalized.setter
    def normalized(self, normalized):
        """Sets the normalized of this EcoSharedMathVector3i.


        :param normalized: The normalized of this EcoSharedMathVector3i.  # noqa: E501
        :type: SystemNumericsVector3
        """

        self._normalized = normalized

    @property
    def normalized_or_zero(self):
        """Gets the normalized_or_zero of this EcoSharedMathVector3i.  # noqa: E501


        :return: The normalized_or_zero of this EcoSharedMathVector3i.  # noqa: E501
        :rtype: SystemNumericsVector3
        """
        return self._normalized_or_zero

    @normalized_or_zero.setter
    def normalized_or_zero(self, normalized_or_zero):
        """Sets the normalized_or_zero of this EcoSharedMathVector3i.


        :param normalized_or_zero: The normalized_or_zero of this EcoSharedMathVector3i.  # noqa: E501
        :type: SystemNumericsVector3
        """

        self._normalized_or_zero = normalized_or_zero

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
        if issubclass(EcoSharedMathVector3i, dict):
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
        if not isinstance(other, EcoSharedMathVector3i):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EcoSharedMathVector3i):
            return True

        return self.to_dict() != other.to_dict()