from __future__ import annotations
import dataclasses
from ..shared import cohort as shared_cohort
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class CohortsPersonsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class CohortsPersonsRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class CohortsPersonsRetrieveQueryParams:
    format: Optional[CohortsPersonsRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class CohortsPersonsRetrieveRequest:
    path_params: CohortsPersonsRetrievePathParams = dataclasses.field()
    query_params: CohortsPersonsRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class CohortsPersonsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    cohort: Optional[shared_cohort.Cohort] = dataclasses.field(default=None)
    