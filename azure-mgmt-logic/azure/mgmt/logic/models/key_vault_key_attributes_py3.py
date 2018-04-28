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


class KeyVaultKeyAttributes(Model):
    """The key attributes.

    :param enabled: Whether the key is enabled or not.
    :type enabled: str
    :param created: When the key was created.
    :type created: long
    :param updated: When the key was updated.
    :type updated: long
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'str'},
        'created': {'key': 'created', 'type': 'long'},
        'updated': {'key': 'updated', 'type': 'long'},
    }

    def __init__(self, *, enabled: str=None, created: int=None, updated: int=None, **kwargs) -> None:
        super(KeyVaultKeyAttributes, self).__init__(**kwargs)
        self.enabled = enabled
        self.created = created
        self.updated = updated
