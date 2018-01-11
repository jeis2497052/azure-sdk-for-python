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

from .nh_resource import NHResource


class NamespaceResource(NHResource):
    """Description of a Namespace resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
    :vartype id: str
    :ivar name: The name of the resource
    :vartype name: str
    :ivar type: The type of the resource. Ex-
     Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The geo-location where the resource lives
    :type location: str
    :param sku: The sku of the created namespace
    :type sku: ~azure.mgmt.notificationhubs.models.Sku
    :param namespace_resource_name: The name of the namespace.
    :type namespace_resource_name: str
    :param provisioning_state: Provisioning state of the Namespace.
    :type provisioning_state: str
    :param region: Specifies the targeted region in which the namespace should
     be created. It can be any of the following values: Australia EastAustralia
     SoutheastCentral USEast USEast US 2West USNorth Central USSouth Central
     USEast AsiaSoutheast AsiaBrazil SouthJapan EastJapan WestNorth EuropeWest
     Europe
    :type region: str
    :param status: Status of the namespace. It can be any of these values:1 =
     Created/Active2 = Creating3 = Suspended4 = Deleting
    :type status: str
    :param created_at: The time the namespace was created.
    :type created_at: datetime
    :param service_bus_endpoint: Endpoint you can use to perform
     NotificationHub operations.
    :type service_bus_endpoint: str
    :param subscription_id: The Id of the Azure subscription associated with
     the namespace.
    :type subscription_id: str
    :param scale_unit: ScaleUnit where the namespace gets created
    :type scale_unit: str
    :param enabled: Whether or not the namespace is currently enabled.
    :type enabled: bool
    :param critical: Whether or not the namespace is set as Critical.
    :type critical: bool
    :param namespace_type: The namespace type. Possible values include:
     'Messaging', 'NotificationHub'
    :type namespace_type: str or
     ~azure.mgmt.notificationhubs.models.NamespaceType
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'namespace_resource_name': {'key': 'properties.name', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'region': {'key': 'properties.region', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
        'service_bus_endpoint': {'key': 'properties.serviceBusEndpoint', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'scale_unit': {'key': 'properties.scaleUnit', 'type': 'str'},
        'enabled': {'key': 'properties.enabled', 'type': 'bool'},
        'critical': {'key': 'properties.critical', 'type': 'bool'},
        'namespace_type': {'key': 'properties.namespaceType', 'type': 'NamespaceType'},
    }

    def __init__(self, location, tags=None, sku=None, namespace_resource_name=None, provisioning_state=None, region=None, status=None, created_at=None, service_bus_endpoint=None, subscription_id=None, scale_unit=None, enabled=None, critical=None, namespace_type=None):
        super(NamespaceResource, self).__init__(tags=tags, location=location, sku=sku)
        self.namespace_resource_name = namespace_resource_name
        self.provisioning_state = provisioning_state
        self.region = region
        self.status = status
        self.created_at = created_at
        self.service_bus_endpoint = service_bus_endpoint
        self.subscription_id = subscription_id
        self.scale_unit = scale_unit
        self.enabled = enabled
        self.critical = critical
        self.namespace_type = namespace_type
