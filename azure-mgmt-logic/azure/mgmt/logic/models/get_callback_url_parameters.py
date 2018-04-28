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


class GetCallbackUrlParameters(Model):
    """The callback url parameters.

    :param not_after: The expiry time.
    :type not_after: datetime
    :param key_type: The key type. Possible values include: 'NotSpecified',
     'Primary', 'Secondary'
    :type key_type: str or ~azure.mgmt.logic.models.KeyType
    """

    _attribute_map = {
        'not_after': {'key': 'notAfter', 'type': 'iso-8601'},
        'key_type': {'key': 'keyType', 'type': 'KeyType'},
    }

    def __init__(self, **kwargs):
        super(GetCallbackUrlParameters, self).__init__(**kwargs)
        self.not_after = kwargs.get('not_after', None)
        self.key_type = kwargs.get('key_type', None)
