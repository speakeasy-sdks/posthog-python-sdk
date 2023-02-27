from __future__ import annotations
import dataclasses
from ..shared import organizationinvite as shared_organizationinvite
from typing import Optional


@dataclasses.dataclass
class InvitesCreatePathParams:
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InvitesCreateRequests:
    organization_invite: Optional[shared_organizationinvite.OrganizationInviteInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    organization_invite1: Optional[shared_organizationinvite.OrganizationInviteInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    organization_invite2: Optional[shared_organizationinvite.OrganizationInviteInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class InvitesCreateRequest:
    path_params: InvitesCreatePathParams = dataclasses.field()
    request: InvitesCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class InvitesCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    organization_invite: Optional[shared_organizationinvite.OrganizationInvite] = dataclasses.field(default=None)
    