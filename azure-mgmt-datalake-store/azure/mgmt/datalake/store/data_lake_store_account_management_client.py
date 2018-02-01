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
from .operations.accounts_operations import AccountsOperations
from .operations.firewall_rules_operations import FirewallRulesOperations
from .operations.trusted_id_providers_operations import TrustedIdProvidersOperations
from .operations.operations import Operations
from .operations.locations_operations import LocationsOperations
from . import models


class DataLakeStoreAccountManagementClientConfiguration(AzureConfiguration):
    """Configuration for DataLakeStoreAccountManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, resource_group_name, account_name, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if resource_group_name is None:
            raise ValueError("Parameter 'resource_group_name' must not be None.")
        if account_name is None:
            raise ValueError("Parameter 'account_name' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(DataLakeStoreAccountManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-datalake-store/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.account_name = account_name


class DataLakeStoreAccountManagementClient(object):
    """Creates an Azure Data Lake Store account management client.

    :ivar config: Configuration for client.
    :vartype config: DataLakeStoreAccountManagementClientConfiguration

    :ivar accounts: Accounts operations
    :vartype accounts: azure.mgmt.datalake.store.operations.AccountsOperations
    :ivar firewall_rules: FirewallRules operations
    :vartype firewall_rules: azure.mgmt.datalake.store.operations.FirewallRulesOperations
    :ivar trusted_id_providers: TrustedIdProviders operations
    :vartype trusted_id_providers: azure.mgmt.datalake.store.operations.TrustedIdProvidersOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datalake.store.operations.Operations
    :ivar locations: Locations operations
    :vartype locations: azure.mgmt.datalake.store.operations.LocationsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure resource group.
    :type resource_group_name: str
    :param account_name: The name of the Data Lake Store account.
    :type account_name: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, resource_group_name, account_name, base_url=None):

        self.config = DataLakeStoreAccountManagementClientConfiguration(credentials, subscription_id, resource_group_name, account_name, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-11-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.accounts = AccountsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.trusted_id_providers = TrustedIdProvidersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.locations = LocationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
