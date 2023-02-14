import dataclasses
from ..shared import paginatedcohortlist as shared_paginatedcohortlist
from typing import Optional


@dataclasses.dataclass
class CohortsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CohortsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CohortsListRequest:
    path_params: CohortsListPathParams = dataclasses.field()
    query_params: CohortsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class CohortsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_cohort_list: Optional[shared_paginatedcohortlist.PaginatedCohortList] = dataclasses.field(default=None)
    