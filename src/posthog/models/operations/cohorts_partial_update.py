import dataclasses
from ..shared import cohort as shared_cohort
from ..shared import patchedcohort as shared_patchedcohort
from typing import Optional


@dataclasses.dataclass
class CohortsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CohortsPartialUpdateRequests:
    patched_cohort: Optional[shared_patchedcohort.PatchedCohortInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_cohort1: Optional[shared_patchedcohort.PatchedCohortInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_cohort2: Optional[shared_patchedcohort.PatchedCohortInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CohortsPartialUpdateRequest:
    path_params: CohortsPartialUpdatePathParams = dataclasses.field()
    request: Optional[CohortsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class CohortsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    cohort: Optional[shared_cohort.Cohort] = dataclasses.field(default=None)
    