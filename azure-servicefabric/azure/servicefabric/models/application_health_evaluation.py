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

from .health_evaluation import HealthEvaluation


class ApplicationHealthEvaluation(HealthEvaluation):
    """Represents health evaluation for an application, containing information
    about the data and the algorithm used by the health store to evaluate
    health.

    :param aggregated_health_state: Possible values include: 'Invalid', 'Ok',
     'Warning', 'Error', 'Unknown'
    :type aggregated_health_state: str or ~azure.servicefabric.models.enum
    :param description: Description of the health evaluation, which represents
     a summary of the evaluation process.
    :type description: str
    :param kind: Constant filled by server.
    :type kind: str
    :param application_name:
    :type application_name: str
    :param unhealthy_evaluations:
    :type unhealthy_evaluations:
     list[~azure.servicefabric.models.HealthEvaluationWrapper]
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'aggregated_health_state': {'key': 'AggregatedHealthState', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'unhealthy_evaluations': {'key': 'UnhealthyEvaluations', 'type': '[HealthEvaluationWrapper]'},
    }

    def __init__(self, aggregated_health_state=None, description=None, application_name=None, unhealthy_evaluations=None):
        super(ApplicationHealthEvaluation, self).__init__(aggregated_health_state=aggregated_health_state, description=description)
        self.application_name = application_name
        self.unhealthy_evaluations = unhealthy_evaluations
        self.kind = 'Application'
