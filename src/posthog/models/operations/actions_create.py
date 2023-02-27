from __future__ import annotations
import dataclasses
from ..shared import action as shared_action
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ActionsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class ActionsCreateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class ActionsCreateQueryParams:
    format: Optional[ActionsCreateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ActionsCreateRequests:
    action: Optional[shared_action.ActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    action1: Optional[shared_action.ActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    action2: Optional[shared_action.ActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ActionsCreateRequest:
    path_params: ActionsCreatePathParams = dataclasses.field()
    query_params: ActionsCreateQueryParams = dataclasses.field()
    request: Optional[ActionsCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class ActionsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    action: Optional[shared_action.Action] = dataclasses.field(default=None)
    body: Optional[bytes] = dataclasses.field(default=None)
    