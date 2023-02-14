import dataclasses
from ..shared import patchedperson as shared_patchedperson
from ..shared import person as shared_person
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsPartialUpdateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsPartialUpdateQueryParams:
    format: Optional[PersonsPartialUpdateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsPartialUpdateRequests:
    patched_person: Optional[shared_patchedperson.PatchedPersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_person1: Optional[shared_patchedperson.PatchedPersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_person2: Optional[shared_patchedperson.PatchedPersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PersonsPartialUpdateRequest:
    path_params: PersonsPartialUpdatePathParams = dataclasses.field()
    query_params: PersonsPartialUpdateQueryParams = dataclasses.field()
    request: Optional[PersonsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PersonsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    