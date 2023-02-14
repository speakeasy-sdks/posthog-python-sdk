import dataclasses
from ..shared import pluginconfig as shared_pluginconfig
from typing import Optional


@dataclasses.dataclass
class PluginConfigsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsRetrieveRequest:
    path_params: PluginConfigsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginConfigsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    plugin_config: Optional[shared_pluginconfig.PluginConfig] = dataclasses.field(default=None)
    