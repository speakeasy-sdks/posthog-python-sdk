import dataclasses
from ..shared import person as shared_person
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsDeletePropertyCreatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsDeletePropertyCreateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsDeletePropertyCreateQueryParams:
    dollar_unset: str = dataclasses.field(metadata={'query_param': { 'field_name': '$unset', 'style': 'form', 'explode': True }})
    format: Optional[PersonsDeletePropertyCreateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsDeletePropertyCreateRequests:
    person: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    person1: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    person2: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PersonsDeletePropertyCreateRequest:
    path_params: PersonsDeletePropertyCreatePathParams = dataclasses.field()
    query_params: PersonsDeletePropertyCreateQueryParams = dataclasses.field()
    request: Optional[PersonsDeletePropertyCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PersonsDeletePropertyCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    