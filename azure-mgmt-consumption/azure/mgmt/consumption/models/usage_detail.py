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

from .resource import Resource


class UsageDetail(Resource):
    """An usage detail resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar billing_period_id: The id of the billing period resource that the
     usage belongs to.
    :vartype billing_period_id: str
    :ivar invoice_id: The id of the invoice resource that the usage belongs
     to.
    :vartype invoice_id: str
    :ivar usage_start: The start of the date time range covered by the usage
     detail.
    :vartype usage_start: datetime
    :ivar usage_end: The end of the date time range covered by the usage
     detail.
    :vartype usage_end: datetime
    :ivar instance_name: The name of the resource instance that the usage is
     about.
    :vartype instance_name: str
    :ivar instance_id: The uri of the resource instance that the usage is
     about.
    :vartype instance_id: str
    :ivar instance_location: The location of the resource instance that the
     usage is about.
    :vartype instance_location: str
    :ivar currency: The ISO currency in which the meter is charged, for
     example, USD.
    :vartype currency: str
    :ivar usage_quantity: The quantity of usage.
    :vartype usage_quantity: decimal.Decimal
    :ivar billable_quantity: The billable usage quantity.
    :vartype billable_quantity: decimal.Decimal
    :ivar pretax_cost: The amount of cost before tax.
    :vartype pretax_cost: decimal.Decimal
    :ivar is_estimated: The estimated usage is subject to change.
    :vartype is_estimated: bool
    :ivar meter_id: The meter id.
    :vartype meter_id: str
    :ivar meter_details: The details about the meter. By default this is not
     populated, unless it's specified in $expand.
    :vartype meter_details: ~azure.mgmt.consumption.models.MeterDetails
    :ivar subscription_guid: Subscription guid.
    :vartype subscription_guid: str
    :ivar subscription_name: Subscription name.
    :vartype subscription_name: str
    :ivar account_name: Account name.
    :vartype account_name: str
    :ivar department_name: Department name.
    :vartype department_name: str
    :ivar product: Product name.
    :vartype product: str
    :ivar consumed_service: Consumed service name.
    :vartype consumed_service: str
    :ivar cost_center: The cost center of this department if it is a
     department and a costcenter exists
    :vartype cost_center: str
    :ivar additional_properties: Additional details of this usage item. By
     default this is not populated, unless it's specified in $expand.
    :vartype additional_properties: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tags': {'readonly': True},
        'billing_period_id': {'readonly': True},
        'invoice_id': {'readonly': True},
        'usage_start': {'readonly': True},
        'usage_end': {'readonly': True},
        'instance_name': {'readonly': True},
        'instance_id': {'readonly': True},
        'instance_location': {'readonly': True},
        'currency': {'readonly': True},
        'usage_quantity': {'readonly': True},
        'billable_quantity': {'readonly': True},
        'pretax_cost': {'readonly': True},
        'is_estimated': {'readonly': True},
        'meter_id': {'readonly': True},
        'meter_details': {'readonly': True},
        'subscription_guid': {'readonly': True},
        'subscription_name': {'readonly': True},
        'account_name': {'readonly': True},
        'department_name': {'readonly': True},
        'product': {'readonly': True},
        'consumed_service': {'readonly': True},
        'cost_center': {'readonly': True},
        'additional_properties': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'billing_period_id': {'key': 'properties.billingPeriodId', 'type': 'str'},
        'invoice_id': {'key': 'properties.invoiceId', 'type': 'str'},
        'usage_start': {'key': 'properties.usageStart', 'type': 'iso-8601'},
        'usage_end': {'key': 'properties.usageEnd', 'type': 'iso-8601'},
        'instance_name': {'key': 'properties.instanceName', 'type': 'str'},
        'instance_id': {'key': 'properties.instanceId', 'type': 'str'},
        'instance_location': {'key': 'properties.instanceLocation', 'type': 'str'},
        'currency': {'key': 'properties.currency', 'type': 'str'},
        'usage_quantity': {'key': 'properties.usageQuantity', 'type': 'decimal'},
        'billable_quantity': {'key': 'properties.billableQuantity', 'type': 'decimal'},
        'pretax_cost': {'key': 'properties.pretaxCost', 'type': 'decimal'},
        'is_estimated': {'key': 'properties.isEstimated', 'type': 'bool'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'meter_details': {'key': 'properties.meterDetails', 'type': 'MeterDetails'},
        'subscription_guid': {'key': 'properties.subscriptionGuid', 'type': 'str'},
        'subscription_name': {'key': 'properties.subscriptionName', 'type': 'str'},
        'account_name': {'key': 'properties.accountName', 'type': 'str'},
        'department_name': {'key': 'properties.departmentName', 'type': 'str'},
        'product': {'key': 'properties.product', 'type': 'str'},
        'consumed_service': {'key': 'properties.consumedService', 'type': 'str'},
        'cost_center': {'key': 'properties.costCenter', 'type': 'str'},
        'additional_properties': {'key': 'properties.additionalProperties', 'type': 'str'},
    }

    def __init__(self):
        super(UsageDetail, self).__init__()
        self.billing_period_id = None
        self.invoice_id = None
        self.usage_start = None
        self.usage_end = None
        self.instance_name = None
        self.instance_id = None
        self.instance_location = None
        self.currency = None
        self.usage_quantity = None
        self.billable_quantity = None
        self.pretax_cost = None
        self.is_estimated = None
        self.meter_id = None
        self.meter_details = None
        self.subscription_guid = None
        self.subscription_name = None
        self.account_name = None
        self.department_name = None
        self.product = None
        self.consumed_service = None
        self.cost_center = None
        self.additional_properties = None
