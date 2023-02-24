from __future__ import annotations
import dataclasses
from ..shared import organizationdomain as shared_organizationdomain
from typing import Optional


@dataclasses.dataclass
class DomainsVerifyCreatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DomainsVerifyCreateRequests:
    organization_domain: Optional[shared_organizationdomain.OrganizationDomainInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    organization_domain1: Optional[shared_organizationdomain.OrganizationDomainInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    organization_domain2: Optional[shared_organizationdomain.OrganizationDomainInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class DomainsVerifyCreateRequest:
    path_params: DomainsVerifyCreatePathParams = dataclasses.field()
    request: DomainsVerifyCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class DomainsVerifyCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_domain: Optional[shared_organizationdomain.OrganizationDomain] = dataclasses.field(default=None)
    