import dataclasses
from ..shared import paginatedorganizationinvitelist as shared_paginatedorganizationinvitelist
from typing import Optional


@dataclasses.dataclass
class InvitesListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InvitesListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InvitesListRequest:
    path_params: InvitesListPathParams = dataclasses.field()
    query_params: InvitesListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class InvitesListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_organization_invite_list: Optional[shared_paginatedorganizationinvitelist.PaginatedOrganizationInviteList] = dataclasses.field(default=None)
    