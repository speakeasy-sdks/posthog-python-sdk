from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class MembersDestroyPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    user_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user__uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MembersDestroyRequest:
    path_params: MembersDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class MembersDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    