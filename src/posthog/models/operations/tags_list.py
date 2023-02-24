from __future__ import annotations
import dataclasses
from ..shared import paginatedtaggeditemlist as shared_paginatedtaggeditemlist
from typing import Optional


@dataclasses.dataclass
class TagsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class TagsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class TagsListRequest:
    path_params: TagsListPathParams = dataclasses.field()
    query_params: TagsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class TagsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_tagged_item_list: Optional[shared_paginatedtaggeditemlist.PaginatedTaggedItemList] = dataclasses.field(default=None)
    