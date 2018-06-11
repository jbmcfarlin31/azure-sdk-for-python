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

from .resource_py3 import Resource


class ServerEndpoint(Resource):
    """Server Endpoint object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The id of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource
    :vartype type: str
    :param server_local_path: Server Local path.
    :type server_local_path: str
    :param cloud_tiering: Cloud Tiering. Possible values include: 'on', 'off'
    :type cloud_tiering: str or ~azure.mgmt.storagesync.models.enum
    :param volume_free_space_percent: Level of free space to be maintained by
     Cloud Tiering if it is enabled.
    :type volume_free_space_percent: int
    :param friendly_name: Friendly Name
    :type friendly_name: str
    :param last_sync_success: Last Sync Success
    :type last_sync_success: datetime
    :param sync_error_state: Sync Error State
    :type sync_error_state: str
    :param sync_error_state_timestamp: Sync Error State Timestamp
    :type sync_error_state_timestamp: datetime
    :param sync_error_direction: Sync Error Direction. Possible values
     include: 'none', 'initialize', 'download', 'upload', 'recall'
    :type sync_error_direction: str or ~azure.mgmt.storagesync.models.enum
    :param item_upload_error_count: Item Upload Error Count.
    :type item_upload_error_count: int
    :param item_download_error_count: Item download error count.
    :type item_download_error_count: int
    :param sync_error_context: sync error context.
    :type sync_error_context: str
    :param current_progress_type: current progress type. Possible values
     include: 'none', 'initialize', 'download', 'upload', 'recall'
    :type current_progress_type: str or ~azure.mgmt.storagesync.models.enum
    :param item_progress_count: Item Progress Count
    :type item_progress_count: int
    :param item_total_count: Item Total Count
    :type item_total_count: int
    :param byte_progress: Bytes in progress
    :type byte_progress: int
    :param total_progress: Total progress
    :type total_progress: int
    :param byte_total: Bytes total
    :type byte_total: int
    :param server_resource_id: Server Resource Id.
    :type server_resource_id: str
    :param provisioning_state: ServerEndpoint Provisioning State
    :type provisioning_state: str
    :param last_workflow_id: ServerEndpoint lastWorkflowId
    :type last_workflow_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'volume_free_space_percent': {'maximum': 100, 'minimum': 0},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'server_local_path': {'key': 'properties.serverLocalPath', 'type': 'str'},
        'cloud_tiering': {'key': 'properties.cloudTiering', 'type': 'str'},
        'volume_free_space_percent': {'key': 'properties.volumeFreeSpacePercent', 'type': 'int'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'last_sync_success': {'key': 'properties.lastSyncSuccess', 'type': 'iso-8601'},
        'sync_error_state': {'key': 'properties.syncErrorState', 'type': 'str'},
        'sync_error_state_timestamp': {'key': 'properties.syncErrorStateTimestamp', 'type': 'iso-8601'},
        'sync_error_direction': {'key': 'properties.syncErrorDirection', 'type': 'str'},
        'item_upload_error_count': {'key': 'properties.itemUploadErrorCount', 'type': 'int'},
        'item_download_error_count': {'key': 'properties.itemDownloadErrorCount', 'type': 'int'},
        'sync_error_context': {'key': 'properties.syncErrorContext', 'type': 'str'},
        'current_progress_type': {'key': 'properties.currentProgressType', 'type': 'str'},
        'item_progress_count': {'key': 'properties.itemProgressCount', 'type': 'int'},
        'item_total_count': {'key': 'properties.itemTotalCount', 'type': 'int'},
        'byte_progress': {'key': 'properties.byteProgress', 'type': 'int'},
        'total_progress': {'key': 'properties.totalProgress', 'type': 'int'},
        'byte_total': {'key': 'properties.byteTotal', 'type': 'int'},
        'server_resource_id': {'key': 'properties.serverResourceId', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'last_workflow_id': {'key': 'properties.lastWorkflowId', 'type': 'str'},
    }

    def __init__(self, *, server_local_path: str=None, cloud_tiering=None, volume_free_space_percent: int=None, friendly_name: str=None, last_sync_success=None, sync_error_state: str=None, sync_error_state_timestamp=None, sync_error_direction=None, item_upload_error_count: int=None, item_download_error_count: int=None, sync_error_context: str=None, current_progress_type=None, item_progress_count: int=None, item_total_count: int=None, byte_progress: int=None, total_progress: int=None, byte_total: int=None, server_resource_id: str=None, provisioning_state: str=None, last_workflow_id: str=None, **kwargs) -> None:
        super(ServerEndpoint, self).__init__(**kwargs)
        self.server_local_path = server_local_path
        self.cloud_tiering = cloud_tiering
        self.volume_free_space_percent = volume_free_space_percent
        self.friendly_name = friendly_name
        self.last_sync_success = last_sync_success
        self.sync_error_state = sync_error_state
        self.sync_error_state_timestamp = sync_error_state_timestamp
        self.sync_error_direction = sync_error_direction
        self.item_upload_error_count = item_upload_error_count
        self.item_download_error_count = item_download_error_count
        self.sync_error_context = sync_error_context
        self.current_progress_type = current_progress_type
        self.item_progress_count = item_progress_count
        self.item_total_count = item_total_count
        self.byte_progress = byte_progress
        self.total_progress = total_progress
        self.byte_total = byte_total
        self.server_resource_id = server_resource_id
        self.provisioning_state = provisioning_state
        self.last_workflow_id = last_workflow_id
