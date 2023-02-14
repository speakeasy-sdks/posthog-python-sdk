import dataclasses
from ..shared import pluginconfig as shared_pluginconfig
from typing import Optional


@dataclasses.dataclass
class PluginConfigsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsCreateRequests:
    plugin_config: Optional[shared_pluginconfig.PluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    plugin_config1: Optional[shared_pluginconfig.PluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    plugin_config2: Optional[shared_pluginconfig.PluginConfigInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PluginConfigsCreateRequest:
    path_params: PluginConfigsCreatePathParams = dataclasses.field()
    request: PluginConfigsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class PluginConfigsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin_config: Optional[shared_pluginconfig.PluginConfig] = dataclasses.field(default=None)
    