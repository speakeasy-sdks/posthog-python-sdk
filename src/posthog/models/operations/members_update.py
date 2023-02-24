from __future__ import annotations
import dataclasses
from ..shared import organizationmember as shared_organizationmember
from typing import Optional


@dataclasses.dataclass
class MembersUpdatePathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    user_uuid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user__uuid', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class MembersUpdateRequests:
    organization_member: Optional[shared_organizationmember.OrganizationMemberInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    organization_member1: Optional[shared_organizationmember.OrganizationMemberInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    organization_member2: Optional[shared_organizationmember.OrganizationMemberInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class MembersUpdateRequest:
    path_params: MembersUpdatePathParams = dataclasses.field()
    request: Optional[MembersUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class MembersUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_member: Optional[shared_organizationmember.OrganizationMember] = dataclasses.field(default=None)
    