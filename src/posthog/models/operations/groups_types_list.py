import dataclasses
from ..shared import grouptype as shared_grouptype
from typing import Optional


@dataclasses.dataclass
class GroupsTypesListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsTypesListRequest:
    path_params: GroupsTypesListPathParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupsTypesListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group_types: Optional[list[shared_grouptype.GroupType]] = dataclasses.field(default=None)
    