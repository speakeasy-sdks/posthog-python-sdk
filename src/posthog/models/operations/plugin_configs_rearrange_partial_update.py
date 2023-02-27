from __future__ import annotations
import dataclasses
from ..shared import patchedpluginconfig as shared_patchedpluginconfig
from ..shared import pluginconfig as shared_pluginconfig
from typing import Optional


@dataclasses.dataclass
class PluginConfigsRearrangePartialUpdatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsRearrangePartialUpdateRequests:
    patched_plugin_config: Optional[shared_patchedpluginconfig.PatchedPluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_plugin_config1: Optional[shared_patchedpluginconfig.PatchedPluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_plugin_config2: Optional[shared_patchedpluginconfig.PatchedPluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PluginConfigsRearrangePartialUpdateRequest:
    path_params: PluginConfigsRearrangePartialUpdatePathParams = dataclasses.field()
    request: Optional[PluginConfigsRearrangePartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PluginConfigsRearrangePartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin_config: Optional[shared_pluginconfig.PluginConfig] = dataclasses.field(default=None)
    