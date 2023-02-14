import dataclasses
from ..shared import paginatedperformanceeventlist as shared_paginatedperformanceeventlist
from typing import Optional


@dataclasses.dataclass
class PerformanceEventsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PerformanceEventsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PerformanceEventsListRequest:
    path_params: PerformanceEventsListPathParams = dataclasses.field()
    query_params: PerformanceEventsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PerformanceEventsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_performance_event_list: Optional[shared_paginatedperformanceeventlist.PaginatedPerformanceEventList] = dataclasses.field(default=None)
    