import dataclasses
from ..shared import paginatedpluginlogentrylist as shared_paginatedpluginlogentrylist
from typing import Optional


@dataclasses.dataclass
class PluginConfigsLogsListPathParams:
    parent_lookup_plugin_config_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_plugin_config_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PluginConfigsLogsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PluginConfigsLogsListRequest:
    path_params: PluginConfigsLogsListPathParams = dataclasses.field()
    query_params: PluginConfigsLogsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PluginConfigsLogsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_plugin_log_entry_list: Optional[shared_paginatedpluginlogentrylist.PaginatedPluginLogEntryList] = dataclasses.field(default=None)
    