import dataclasses
from ..shared import team as shared_team
from typing import Optional


@dataclasses.dataclass
class RetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RetrieveRequest:
    path_params: RetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class RetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    team: Optional[shared_team.Team] = dataclasses.field(default=None)
    