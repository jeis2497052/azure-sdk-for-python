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

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.namespaces_operations import NamespacesOperations
from .operations.authorization_rules_operations import AuthorizationRulesOperations
from .operations.notification_hubs_operations import NotificationHubsOperations
from .operations.hub_authorization_rules_operations import HubAuthorizationRulesOperations
from . import models


class NotificationHubsManagementClientConfiguration(AzureConfiguration):
    """Configuration for NotificationHubsManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(NotificationHubsManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-notificationhubs/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class NotificationHubsManagementClient(object):
    """Azure NotificationHub client

    :ivar config: Configuration for client.
    :vartype config: NotificationHubsManagementClientConfiguration

    :ivar namespaces: Namespaces operations
    :vartype namespaces: azure.mgmt.notificationhubs.operations.NamespacesOperations
    :ivar authorization_rules: AuthorizationRules operations
    :vartype authorization_rules: azure.mgmt.notificationhubs.operations.AuthorizationRulesOperations
    :ivar notification_hubs: NotificationHubs operations
    :vartype notification_hubs: azure.mgmt.notificationhubs.operations.NotificationHubsOperations
    :ivar hub_authorization_rules: HubAuthorizationRules operations
    :vartype hub_authorization_rules: azure.mgmt.notificationhubs.operations.HubAuthorizationRulesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = NotificationHubsManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2017-11-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.namespaces = NamespacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.authorization_rules = AuthorizationRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.notification_hubs = NotificationHubsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hub_authorization_rules = HubAuthorizationRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
