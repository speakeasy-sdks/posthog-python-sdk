import dataclasses
from ..shared import person as shared_person
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsFunnelCorrelationRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsFunnelCorrelationRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsFunnelCorrelationRetrieveQueryParams:
    format: Optional[PersonsFunnelCorrelationRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsFunnelCorrelationRetrieveRequest:
    path_params: PersonsFunnelCorrelationRetrievePathParams = dataclasses.field()
    query_params: PersonsFunnelCorrelationRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PersonsFunnelCorrelationRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    person: Optional[shared_person.Person] = dataclasses.field(default=None)
    