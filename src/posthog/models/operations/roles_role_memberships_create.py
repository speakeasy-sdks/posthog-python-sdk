from __future__ import annotations
import dataclasses
from ..shared import rolemembership as shared_rolemembership
from typing import Optional


@dataclasses.dataclass
class RolesRoleMembershipsCreatePathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    parent_lookup_role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_role_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesRoleMembershipsCreateRequests:
    role_membership: Optional[shared_rolemembership.RoleMembershipInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    role_membership1: Optional[shared_rolemembership.RoleMembershipInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    role_membership2: Optional[shared_rolemembership.RoleMembershipInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class RolesRoleMembershipsCreateRequest:
    path_params: RolesRoleMembershipsCreatePathParams = dataclasses.field()
    request: RolesRoleMembershipsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class RolesRoleMembershipsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    role_membership: Optional[shared_rolemembership.RoleMembershipOutput] = dataclasses.field(default=None)
    