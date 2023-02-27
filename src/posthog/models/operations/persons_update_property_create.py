from __future__ import annotations
import dataclasses
from ..shared import person as shared_person
from enum import Enum
from typing import Any, Optional


@dataclasses.dataclass
class PersonsUpdatePropertyCreatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsUpdatePropertyCreateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsUpdatePropertyCreateQueryParams:
    key: str = dataclasses.field(metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    value: Any = dataclasses.field(metadata={'query_param': { 'field_name': 'value', 'style': 'form', 'explode': True }})
    format: Optional[PersonsUpdatePropertyCreateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsUpdatePropertyCreateRequests:
    person: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    person1: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    person2: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PersonsUpdatePropertyCreateRequest:
    path_params: PersonsUpdatePropertyCreatePathParams = dataclasses.field()
    query_params: PersonsUpdatePropertyCreateQueryParams = dataclasses.field()
    request: Optional[PersonsUpdatePropertyCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PersonsUpdatePropertyCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    