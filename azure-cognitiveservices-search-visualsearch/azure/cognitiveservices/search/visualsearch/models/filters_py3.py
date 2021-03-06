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


class Filters(Model):
    """A key-value object consisting of filters that may be specified to limit the
    results returned by the API. Current available filters: site.

    :param site: The URL of the site to return similar images and similar
     products from. (e.g., "www.bing.com", "bing.com").
    :type site: str
    """

    _attribute_map = {
        'site': {'key': 'site', 'type': 'str'},
    }

    def __init__(self, *, site: str=None, **kwargs) -> None:
        super(Filters, self).__init__(**kwargs)
        self.site = site
