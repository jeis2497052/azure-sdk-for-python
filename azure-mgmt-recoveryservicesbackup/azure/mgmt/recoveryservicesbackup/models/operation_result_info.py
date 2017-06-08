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

from .operation_result_info_base import OperationResultInfoBase


class OperationResultInfo(OperationResultInfoBase):
    """Operation result info.

    :param object_type: Polymorphic Discriminator
    :type object_type: str
    :param job_list: List of jobs created by this operation.
    :type job_list: list of str
    """

    _validation = {
        'object_type': {'required': True},
    }

    _attribute_map = {
        'object_type': {'key': 'objectType', 'type': 'str'},
        'job_list': {'key': 'jobList', 'type': '[str]'},
    }

    def __init__(self, job_list=None):
        super(OperationResultInfo, self).__init__()
        self.job_list = job_list
        self.object_type = 'OperationResultInfo'