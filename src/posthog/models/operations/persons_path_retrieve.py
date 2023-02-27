from __future__ import annotations
import dataclasses
from ..shared import person as shared_person
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsPathRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsPathRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsPathRetrieveQueryParams:
    format: Optional[PersonsPathRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsPathRetrieveRequest:
    path_params: PersonsPathRetrievePathParams = dataclasses.field()
    query_params: PersonsPathRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PersonsPathRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    