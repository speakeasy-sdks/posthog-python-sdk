from __future__ import annotations
import dataclasses
from ..shared import patchedplugin as shared_patchedplugin
from ..shared import plugin as shared_plugin
from typing import Optional


@dataclasses.dataclass
class PluginsUpdateSourcePartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginsUpdateSourcePartialUpdateRequests:
    patched_plugin: Optional[shared_patchedplugin.PatchedPluginInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_plugin1: Optional[shared_patchedplugin.PatchedPluginInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_plugin2: Optional[shared_patchedplugin.PatchedPluginInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PluginsUpdateSourcePartialUpdateRequest:
    path_params: PluginsUpdateSourcePartialUpdatePathParams = dataclasses.field()
    request: Optional[PluginsUpdateSourcePartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PluginsUpdateSourcePartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin: Optional[shared_plugin.Plugin] = dataclasses.field(default=None)
    