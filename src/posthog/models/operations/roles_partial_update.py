from __future__ import annotations
import dataclasses
from ..shared import patchedrole as shared_patchedrole
from ..shared import role as shared_role
from typing import Optional


@dataclasses.dataclass
class RolesPartialUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesPartialUpdateRequests:
    patched_role: Optional[shared_patchedrole.PatchedRoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_role1: Optional[shared_patchedrole.PatchedRoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_role2: Optional[shared_patchedrole.PatchedRoleInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class RolesPartialUpdateRequest:
    path_params: RolesPartialUpdatePathParams = dataclasses.field()
    request: Optional[RolesPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class RolesPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    role: Optional[shared_role.Role] = dataclasses.field(default=None)
    