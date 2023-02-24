from __future__ import annotations
import dataclasses
from ..shared import paginatedrolelist as shared_paginatedrolelist
from typing import Optional


@dataclasses.dataclass
class RolesListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class RolesListRequest:
    path_params: RolesListPathParams = dataclasses.field()
    query_params: RolesListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class RolesListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_role_list: Optional[shared_paginatedrolelist.PaginatedRoleList] = dataclasses.field(default=None)
    