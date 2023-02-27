from __future__ import annotations
import dataclasses
from ..shared import role as shared_role
from typing import Optional


@dataclasses.dataclass
class RolesUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesUpdateRequests:
    role: Optional[shared_role.RoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    role1: Optional[shared_role.RoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    role2: Optional[shared_role.RoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class RolesUpdateRequest:
    path_params: RolesUpdatePathParams = dataclasses.field()
    request: RolesUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class RolesUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    role: Optional[shared_role.Role] = dataclasses.field(default=None)
    