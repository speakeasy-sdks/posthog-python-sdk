import dataclasses
from ..shared import organizationresourceaccess as shared_organizationresourceaccess
from typing import Optional


@dataclasses.dataclass
class ResourceAccessRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResourceAccessRetrieveRequest:
    path_params: ResourceAccessRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class ResourceAccessRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_resource_access: Optional[shared_organizationresourceaccess.OrganizationResourceAccess] = dataclasses.field(default=None)
    