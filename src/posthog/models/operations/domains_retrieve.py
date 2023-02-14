import dataclasses
from ..shared import organizationdomain as shared_organizationdomain
from typing import Optional


@dataclasses.dataclass
class DomainsRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DomainsRetrieveRequest:
    path_params: DomainsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class DomainsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_domain: Optional[shared_organizationdomain.OrganizationDomain] = dataclasses.field(default=None)
    