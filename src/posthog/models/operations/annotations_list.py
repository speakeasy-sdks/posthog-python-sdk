from __future__ import annotations
import dataclasses
from ..shared import paginatedannotationlist as shared_paginatedannotationlist
from typing import Optional


@dataclasses.dataclass
class AnnotationsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AnnotationsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class AnnotationsListRequest:
    path_params: AnnotationsListPathParams = dataclasses.field()
    query_params: AnnotationsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class AnnotationsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_annotation_list: Optional[shared_paginatedannotationlist.PaginatedAnnotationList] = dataclasses.field(default=None)
    