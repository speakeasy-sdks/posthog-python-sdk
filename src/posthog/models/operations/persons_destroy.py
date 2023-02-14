import dataclasses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PersonsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PersonsDestroyFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class PersonsDestroyQueryParams:
    delete_events: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'delete_events', 'style': 'form', 'explode': True }})
    format: Optional[PersonsDestroyFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PersonsDestroyRequest:
    path_params: PersonsDestroyPathParams = dataclasses.field()
    query_params: PersonsDestroyQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PersonsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    