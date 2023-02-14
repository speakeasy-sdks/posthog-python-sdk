import dataclasses
from ..shared import paginateddashboardlist as shared_paginateddashboardlist
from typing import Optional


@dataclasses.dataclass
class DashboardsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DashboardsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class DashboardsListRequest:
    path_params: DashboardsListPathParams = dataclasses.field()
    query_params: DashboardsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class DashboardsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_dashboard_list: Optional[shared_paginateddashboardlist.PaginatedDashboardList] = dataclasses.field(default=None)
    