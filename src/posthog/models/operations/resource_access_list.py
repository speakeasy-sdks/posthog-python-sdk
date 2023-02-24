from __future__ import annotations
import dataclasses
from ..shared import paginatedorganizationresourceaccesslist as shared_paginatedorganizationresourceaccesslist
from typing import Optional


@dataclasses.dataclass
class ResourceAccessListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResourceAccessListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ResourceAccessListRequest:
    path_params: ResourceAccessListPathParams = dataclasses.field()
    query_params: ResourceAccessListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ResourceAccessListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_organization_resource_access_list: Optional[shared_paginatedorganizationresourceaccesslist.PaginatedOrganizationResourceAccessList] = dataclasses.field(default=None)
    