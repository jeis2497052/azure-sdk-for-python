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

from msrest.serialization import Model


class Credential(Model):
    """Definition of the credential.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Gets the id of the resource.
    :vartype id: str
    :param name: Gets the name of the credential.
    :type name: str
    :ivar user_name: Gets the user name of the credential.
    :vartype user_name: str
    :ivar creation_time: Gets the creation time.
    :vartype creation_time: datetime
    :ivar last_modified_time: Gets the last modified time.
    :vartype last_modified_time: datetime
    :param description: Gets or sets the description.
    :type description: str
    """

    _validation = {
        'id': {'readonly': True},
        'user_name': {'readonly': True},
        'creation_time': {'readonly': True},
        'last_modified_time': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'description': {'key': 'properties.description', 'type': 'str'},
    }

    def __init__(self, name=None, description=None):
        super(Credential, self).__init__()
        self.id = None
        self.name = name
        self.user_name = None
        self.creation_time = None
        self.last_modified_time = None
        self.description = description
