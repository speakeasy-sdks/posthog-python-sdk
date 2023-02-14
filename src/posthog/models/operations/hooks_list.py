import dataclasses
from ..shared import paginatedhooklist as shared_paginatedhooklist
from typing import Optional


@dataclasses.dataclass
class HooksListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HooksListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class HooksListRequest:
    path_params: HooksListPathParams = dataclasses.field()
    query_params: HooksListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class HooksListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_hook_list: Optional[shared_paginatedhooklist.PaginatedHookList] = dataclasses.field(default=None)
    