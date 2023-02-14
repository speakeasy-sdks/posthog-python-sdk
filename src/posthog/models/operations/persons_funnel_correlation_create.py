import dataclasses
from ..shared import person as shared_person
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsFunnelCorrelationCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsFunnelCorrelationCreateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsFunnelCorrelationCreateQueryParams:
    format: Optional[PersonsFunnelCorrelationCreateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsFunnelCorrelationCreateRequests:
    person: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    person1: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    person2: Optional[shared_person.PersonInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PersonsFunnelCorrelationCreateRequest:
    path_params: PersonsFunnelCorrelationCreatePathParams = dataclasses.field()
    query_params: PersonsFunnelCorrelationCreateQueryParams = dataclasses.field()
    request: Optional[PersonsFunnelCorrelationCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PersonsFunnelCorrelationCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    