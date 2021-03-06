# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .dataset_partition_value import DatasetPartitionValue


class DatasetDateTimePartitionValue(DatasetPartitionValue):
    """The date/time value of a partition.

    :param type: Polymorphic Discriminator
    :type type: str
    :param date_property: Name of variable containing date. Type: string (or
     Expression with resultType string).
    :type date_property: object
    :param format: Format string for the Date value. Type: string (or
     Expression with resultType string).
    :type format: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'date_property': {'key': 'date', 'type': 'object'},
        'format': {'key': 'format', 'type': 'object'},
    }

    def __init__(self, date_property=None, format=None):
        super(DatasetDateTimePartitionValue, self).__init__()
        self.date_property = date_property
        self.format = format
        self.type = 'DateTime'
