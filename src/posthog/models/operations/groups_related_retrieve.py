from __future__ import annotations
import dataclasses
from ..shared import group as shared_group
from typing import Optional


@dataclasses.dataclass
class GroupsRelatedRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsRelatedRetrieveQueryParams:
    group_type_index: int = dataclasses.field(metadata={'query_param': { 'field_name': 'group_type_index', 'style': 'form', 'explode': True }})
    id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GroupsRelatedRetrieveRequest:
    path_params: GroupsRelatedRetrievePathParams = dataclasses.field()
    query_params: GroupsRelatedRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupsRelatedRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group: Optional[shared_group.Group] = dataclasses.field(default=None)
    