import dataclasses
from ..shared import plugin as shared_plugin
from typing import Optional


@dataclasses.dataclass
class PluginsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginsRetrieveRequest:
    path_params: PluginsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin: Optional[shared_plugin.Plugin] = dataclasses.field(default=None)
    