import dataclasses
from ..shared import cohort as shared_cohort
from typing import Optional


@dataclasses.dataclass
class CohortsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CohortsRetrieveRequest:
    path_params: CohortsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class CohortsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    cohort: Optional[shared_cohort.Cohort] = dataclasses.field(default=None)
    