import dataclasses
from ..shared import organizationresourceaccess as shared_organizationresourceaccess
from ..shared import patchedorganizationresourceaccess as shared_patchedorganizationresourceaccess
from typing import Optional


@dataclasses.dataclass
class ResourceAccessPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResourceAccessPartialUpdateRequests:
    patched_organization_resource_access: Optional[shared_patchedorganizationresourceaccess.PatchedOrganizationResourceAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_organization_resource_access1: Optional[shared_patchedorganizationresourceaccess.PatchedOrganizationResourceAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_organization_resource_access2: Optional[shared_patchedorganizationresourceaccess.PatchedOrganizationResourceAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ResourceAccessPartialUpdateRequest:
    path_params: ResourceAccessPartialUpdatePathParams = dataclasses.field()
    request: Optional[ResourceAccessPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class ResourceAccessPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_resource_access: Optional[shared_organizationresourceaccess.OrganizationResourceAccess] = dataclasses.field(default=None)
    