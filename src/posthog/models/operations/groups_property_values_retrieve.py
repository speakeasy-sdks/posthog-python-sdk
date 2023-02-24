from __future__ import annotations
import dataclasses
from ..shared import group as shared_group
from typing import Optional


@dataclasses.dataclass
class GroupsPropertyValuesRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsPropertyValuesRetrieveQueryParams:
    group_type_index: int = dataclasses.field(metadata={'query_param': { 'field_name': 'group_type_index', 'style': 'form', 'explode': True }})
    key: str = dataclasses.field(metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GroupsPropertyValuesRetrieveRequest:
    path_params: GroupsPropertyValuesRetrievePathParams = dataclasses.field()
    query_params: GroupsPropertyValuesRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupsPropertyValuesRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group: Optional[shared_group.Group] = dataclasses.field(default=None)
    