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


class CreateOrUpdateTrustedIdProviderParameters(Model):
    """The parameters used to create a new trusted identity provider.

    :param id_provider: The URL of this trusted identity provider.
    :type id_provider: str
    """

    _validation = {
        'id_provider': {'required': True},
    }

    _attribute_map = {
        'id_provider': {'key': 'properties.idProvider', 'type': 'str'},
    }

    def __init__(self, id_provider):
        super(CreateOrUpdateTrustedIdProviderParameters, self).__init__()
        self.id_provider = id_provider
