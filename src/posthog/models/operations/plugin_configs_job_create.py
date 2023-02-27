from __future__ import annotations
import dataclasses
from ..shared import pluginconfig as shared_pluginconfig
from typing import Optional


@dataclasses.dataclass
class PluginConfigsJobCreatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsJobCreateRequests:
    plugin_config: Optional[shared_pluginconfig.PluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    plugin_config1: Optional[shared_pluginconfig.PluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    plugin_config2: Optional[shared_pluginconfig.PluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PluginConfigsJobCreateRequest:
    path_params: PluginConfigsJobCreatePathParams = dataclasses.field()
    request: PluginConfigsJobCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class PluginConfigsJobCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin_config: Optional[shared_pluginconfig.PluginConfig] = dataclasses.field(default=None)
    