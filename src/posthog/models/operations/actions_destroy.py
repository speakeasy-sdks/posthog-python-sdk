from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ActionsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class ActionsDestroyFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class ActionsDestroyQueryParams:
    format: Optional[ActionsDestroyFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ActionsDestroyRequest:
    path_params: ActionsDestroyPathParams = dataclasses.field()
    query_params: ActionsDestroyQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ActionsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    