from __future__ import annotations
import dataclasses
from ..shared import paginatedpluginconfiglist as shared_paginatedpluginconfiglist
from typing import Optional


@dataclasses.dataclass
class PluginConfigsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PluginConfigsListRequest:
    path_params: PluginConfigsListPathParams = dataclasses.field()
    query_params: PluginConfigsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginConfigsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_plugin_config_list: Optional[shared_paginatedpluginconfiglist.PaginatedPluginConfigList] = dataclasses.field(default=None)
    