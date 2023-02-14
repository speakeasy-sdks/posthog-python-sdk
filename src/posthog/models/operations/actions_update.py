import dataclasses
from ..shared import action as shared_action
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ActionsUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class ActionsUpdateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class ActionsUpdateQueryParams:
    format: Optional[ActionsUpdateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ActionsUpdateRequests:
    action: Optional[shared_action.ActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    action1: Optional[shared_action.ActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    action2: Optional[shared_action.ActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ActionsUpdateRequest:
    path_params: ActionsUpdatePathParams = dataclasses.field()
    query_params: ActionsUpdateQueryParams = dataclasses.field()
    request: Optional[ActionsUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class ActionsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    action: Optional[shared_action.Action] = dataclasses.field(default=None)
    body: Optional[bytes] = dataclasses.field(default=None)
    