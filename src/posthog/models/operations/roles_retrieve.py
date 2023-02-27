from __future__ import annotations
import dataclasses
from ..shared import role as shared_role
from typing import Optional


@dataclasses.dataclass
class RolesRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesRetrieveRequest:
    path_params: RolesRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class RolesRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    role: Optional[shared_role.Role] = dataclasses.field(default=None)
    