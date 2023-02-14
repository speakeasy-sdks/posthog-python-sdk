import dataclasses
from ..shared import paginatedorganizationdomainlist as shared_paginatedorganizationdomainlist
from typing import Optional


@dataclasses.dataclass
class DomainsListPathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DomainsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class DomainsListRequest:
    path_params: DomainsListPathParams = dataclasses.field()
    query_params: DomainsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class DomainsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_organization_domain_list: Optional[shared_paginatedorganizationdomainlist.PaginatedOrganizationDomainList] = dataclasses.field(default=None)
    