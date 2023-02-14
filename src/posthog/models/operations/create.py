import dataclasses
from ..shared import team as shared_team
from typing import Optional


@dataclasses.dataclass
class CreateRequests:
    team: Optional[shared_team.TeamInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    team1: Optional[shared_team.TeamInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    team2: Optional[shared_team.TeamInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CreateRequest:
    request: Optional[CreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class CreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    team: Optional[shared_team.Team] = dataclasses.field(default=None)
    