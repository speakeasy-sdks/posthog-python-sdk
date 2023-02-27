from __future__ import annotations
import dataclasses
from ..shared import patchedteam as shared_patchedteam
from ..shared import team as shared_team
from typing import Optional


@dataclasses.dataclass
class PartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PartialUpdateRequests:
    patched_team: Optional[shared_patchedteam.PatchedTeamInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_team1: Optional[shared_patchedteam.PatchedTeamInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_team2: Optional[shared_patchedteam.PatchedTeamInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PartialUpdateRequest:
    path_params: PartialUpdatePathParams = dataclasses.field()
    request: Optional[PartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    team: Optional[shared_team.Team] = dataclasses.field(default=None)
    