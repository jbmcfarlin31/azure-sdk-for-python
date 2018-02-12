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


class SourceControlSyncJobByIdErrors(Model):
    """Error details of the source control sync job.

    :param code: Gets the error code for the job.
    :type code: str
    :param message: Gets the error message for the job.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, code=None, message=None):
        super(SourceControlSyncJobByIdErrors, self).__init__()
        self.code = code
        self.message = message
