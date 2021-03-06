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


class BackupPartitionDescription(Model):
    """Describes the parameters for triggering partition's backup.

    :param backup_storage: Specifies the details of the backup storage where
     to save the backup.
    :type backup_storage: ~azure.servicefabric.models.BackupStorageDescription
    """

    _attribute_map = {
        'backup_storage': {'key': 'BackupStorage', 'type': 'BackupStorageDescription'},
    }

    def __init__(self, **kwargs):
        super(BackupPartitionDescription, self).__init__(**kwargs)
        self.backup_storage = kwargs.get('backup_storage', None)
