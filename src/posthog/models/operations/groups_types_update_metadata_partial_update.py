import dataclasses
from ..shared import grouptype as shared_grouptype
from ..shared import patchedgrouptype as shared_patchedgrouptype
from typing import Optional


@dataclasses.dataclass
class GroupsTypesUpdateMetadataPartialUpdatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class GroupsTypesUpdateMetadataPartialUpdateRequests:
    patched_group_type: Optional[shared_patchedgrouptype.PatchedGroupTypeInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_group_type1: Optional[shared_patchedgrouptype.PatchedGroupTypeInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_group_type2: Optional[shared_patchedgrouptype.PatchedGroupTypeInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class GroupsTypesUpdateMetadataPartialUpdateRequest:
    path_params: GroupsTypesUpdateMetadataPartialUpdatePathParams = dataclasses.field()
    request: Optional[GroupsTypesUpdateMetadataPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class GroupsTypesUpdateMetadataPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    group_type: Optional[shared_grouptype.GroupType] = dataclasses.field(default=None)
    