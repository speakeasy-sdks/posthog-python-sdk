import dataclasses
from ..shared import group as shared_group
from typing import Optional


@dataclasses.dataclass
class GroupsFindRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsFindRetrieveQueryParams:
    group_key: str = dataclasses.field(metadata={'query_param': { 'field_name': 'group_key', 'style': 'form', 'explode': True }})
    group_type_index: int = dataclasses.field(metadata={'query_param': { 'field_name': 'group_type_index', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class GroupsFindRetrieveRequest:
    path_params: GroupsFindRetrievePathParams = dataclasses.field()
    query_params: GroupsFindRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupsFindRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group: Optional[shared_group.Group] = dataclasses.field(default=None)
    