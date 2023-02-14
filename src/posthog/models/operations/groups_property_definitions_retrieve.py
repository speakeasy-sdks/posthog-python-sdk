import dataclasses
from ..shared import group as shared_group
from typing import Optional


@dataclasses.dataclass
class GroupsPropertyDefinitionsRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsPropertyDefinitionsRetrieveRequest:
    path_params: GroupsPropertyDefinitionsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class GroupsPropertyDefinitionsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group: Optional[shared_group.Group] = dataclasses.field(default=None)
    