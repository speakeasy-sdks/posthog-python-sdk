from __future__ import annotations
import dataclasses
from ..shared import person as shared_person
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsPropertiesTimelineRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsPropertiesTimelineRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsPropertiesTimelineRetrieveQueryParams:
    format: Optional[PersonsPropertiesTimelineRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsPropertiesTimelineRetrieveRequest:
    path_params: PersonsPropertiesTimelineRetrievePathParams = dataclasses.field()
    query_params: PersonsPropertiesTimelineRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PersonsPropertiesTimelineRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    