from __future__ import annotations
import dataclasses
from ..shared import organizationresourceaccess as shared_organizationresourceaccess
from typing import Optional


@dataclasses.dataclass
class ResourceAccessUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResourceAccessUpdateRequests:
    organization_resource_access: Optional[shared_organizationresourceaccess.OrganizationResourceAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    organization_resource_access1: Optional[shared_organizationresourceaccess.OrganizationResourceAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    organization_resource_access2: Optional[shared_organizationresourceaccess.OrganizationResourceAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ResourceAccessUpdateRequest:
    path_params: ResourceAccessUpdatePathParams = dataclasses.field()
    request: ResourceAccessUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class ResourceAccessUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_resource_access: Optional[shared_organizationresourceaccess.OrganizationResourceAccess] = dataclasses.field(default=None)
    