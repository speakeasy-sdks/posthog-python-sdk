from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class RolesRoleMembershipsDestroyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    parent_lookup_role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_role_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesRoleMembershipsDestroyRequest:
    path_params: RolesRoleMembershipsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RolesRoleMembershipsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    