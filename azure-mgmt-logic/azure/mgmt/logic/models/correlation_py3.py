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


class Correlation(Model):
    """The correlation property.

    :param client_tracking_id: The client tracking id.
    :type client_tracking_id: str
    """

    _attribute_map = {
        'client_tracking_id': {'key': 'clientTrackingId', 'type': 'str'},
    }

    def __init__(self, *, client_tracking_id: str=None, **kwargs) -> None:
        super(Correlation, self).__init__(**kwargs)
        self.client_tracking_id = client_tracking_id
