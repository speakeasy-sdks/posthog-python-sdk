import dataclasses
from ..shared import paginatedpluginlist as shared_paginatedpluginlist
from typing import Optional


@dataclasses.dataclass
class PluginsListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PluginsListRequest:
    path_params: PluginsListPathParams = dataclasses.field()
    query_params: PluginsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_plugin_list: Optional[shared_paginatedpluginlist.PaginatedPluginList] = dataclasses.field(default=None)
    