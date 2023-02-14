import dataclasses
from ..shared import organizationmember as shared_organizationmember
from ..shared import patchedorganizationmember as shared_patchedorganizationmember
from typing import Optional


@dataclasses.dataclass
class MembersPartialUpdatePathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    user_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user__uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MembersPartialUpdateRequests:
    patched_organization_member: Optional[shared_patchedorganizationmember.PatchedOrganizationMemberInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_organization_member1: Optional[shared_patchedorganizationmember.PatchedOrganizationMemberInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_organization_member2: Optional[shared_patchedorganizationmember.PatchedOrganizationMemberInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class MembersPartialUpdateRequest:
    path_params: MembersPartialUpdatePathParams = dataclasses.field()
    request: Optional[MembersPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class MembersPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_member: Optional[shared_organizationmember.OrganizationMember] = dataclasses.field(default=None)
    