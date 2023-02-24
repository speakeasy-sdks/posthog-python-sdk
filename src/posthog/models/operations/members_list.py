from __future__ import annotations
import dataclasses
from ..shared import paginatedorganizationmemberlist as shared_paginatedorganizationmemberlist
from typing import Optional


@dataclasses.dataclass
class MembersListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MembersListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class MembersListRequest:
    path_params: MembersListPathParams = dataclasses.field()
    query_params: MembersListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class MembersListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_organization_member_list: Optional[shared_paginatedorganizationmemberlist.PaginatedOrganizationMemberList] = dataclasses.field(default=None)
    