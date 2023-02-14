import dataclasses
from ..shared import paginatedrolemembershiplist as shared_paginatedrolemembershiplist
from typing import Optional


@dataclasses.dataclass
class RolesRoleMembershipsListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    parent_lookup_role_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_role_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesRoleMembershipsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class RolesRoleMembershipsListRequest:
    path_params: RolesRoleMembershipsListPathParams = dataclasses.field()
    query_params: RolesRoleMembershipsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class RolesRoleMembershipsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_role_membership_list: Optional[shared_paginatedrolemembershiplist.PaginatedRoleMembershipList] = dataclasses.field(default=None)
    