import dataclasses
from ..shared import organizationdomain as shared_organizationdomain
from ..shared import patchedorganizationdomain as shared_patchedorganizationdomain
from typing import Optional


@dataclasses.dataclass
class DomainsPartialUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DomainsPartialUpdateRequests:
    patched_organization_domain: Optional[shared_patchedorganizationdomain.PatchedOrganizationDomainInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_organization_domain1: Optional[shared_patchedorganizationdomain.PatchedOrganizationDomainInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_organization_domain2: Optional[shared_patchedorganizationdomain.PatchedOrganizationDomainInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class DomainsPartialUpdateRequest:
    path_params: DomainsPartialUpdatePathParams = dataclasses.field()
    request: Optional[DomainsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class DomainsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_domain: Optional[shared_organizationdomain.OrganizationDomain] = dataclasses.field(default=None)
    