from __future__ import annotations
import dataclasses
from ..shared import paginatedgrouplist as shared_paginatedgrouplist
from typing import Optional


@dataclasses.dataclass
class GroupsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsListQueryParams:
    group_type_index: int = dataclasses.field(metadata={'query_param': { 'field_name': 'group_type_index', 'style': 'form', 'explode': True }})
    cursor: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GroupsListRequest:
    path_params: GroupsListPathParams = dataclasses.field()
    query_params: GroupsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_group_list: Optional[shared_paginatedgrouplist.PaginatedGroupList] = dataclasses.field(default=None)
    