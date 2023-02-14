import dataclasses
from ..shared import plugin as shared_plugin
from typing import Optional


@dataclasses.dataclass
class PluginsUpgradeCreatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginsUpgradeCreateRequests:
    plugin: Optional[shared_plugin.PluginInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    plugin1: Optional[shared_plugin.PluginInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    plugin2: Optional[shared_plugin.PluginInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PluginsUpgradeCreateRequest:
    path_params: PluginsUpgradeCreatePathParams = dataclasses.field()
    request: Optional[PluginsUpgradeCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PluginsUpgradeCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin: Optional[shared_plugin.Plugin] = dataclasses.field(default=None)
    