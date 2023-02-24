from __future__ import annotations
import dataclasses
from ..shared import action as shared_action
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ActionsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class ActionsRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class ActionsRetrieveQueryParams:
    format: Optional[ActionsRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ActionsRetrieveRequest:
    path_params: ActionsRetrievePathParams = dataclasses.field()
    query_params: ActionsRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ActionsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    action: Optional[shared_action.Action] = dataclasses.field(default=None)
    body: Optional[bytes] = dataclasses.field(default=None)
    