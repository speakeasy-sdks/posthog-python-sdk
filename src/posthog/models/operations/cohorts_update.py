from __future__ import annotations
import dataclasses
from ..shared import cohort as shared_cohort
from typing import Optional


@dataclasses.dataclass
class CohortsUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CohortsUpdateRequests:
    cohort: Optional[shared_cohort.CohortInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    cohort1: Optional[shared_cohort.CohortInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    cohort2: Optional[shared_cohort.CohortInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class CohortsUpdateRequest:
    path_params: CohortsUpdatePathParams = dataclasses.field()
    request: Optional[CohortsUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class CohortsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    cohort: Optional[shared_cohort.Cohort] = dataclasses.field(default=None)
    