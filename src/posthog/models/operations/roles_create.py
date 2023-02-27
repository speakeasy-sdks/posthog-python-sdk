from __future__ import annotations
import dataclasses
from ..shared import role as shared_role
from typing import Optional


@dataclasses.dataclass
class RolesCreatePathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesCreateRequests:
    role: Optional[shared_role.RoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    role1: Optional[shared_role.RoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    role2: Optional[shared_role.RoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class RolesCreateRequest:
    path_params: RolesCreatePathParams = dataclasses.field()
    request: RolesCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class RolesCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    role: Optional[shared_role.Role] = dataclasses.field(default=None)
    