from __future__ import annotations
import dataclasses
from ..shared import plugin as shared_plugin
from typing import Optional


@dataclasses.dataclass
class PluginsActivityRetrievePathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginsActivityRetrieveRequest:
    path_params: PluginsActivityRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginsActivityRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin: Optional[shared_plugin.Plugin] = dataclasses.field(default=None)
    