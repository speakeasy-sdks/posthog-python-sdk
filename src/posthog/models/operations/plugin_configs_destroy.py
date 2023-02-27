from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class PluginConfigsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsDestroyRequest:
    path_params: PluginConfigsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginConfigsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    