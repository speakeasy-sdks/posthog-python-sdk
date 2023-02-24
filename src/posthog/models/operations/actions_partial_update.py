from __future__ import annotations
import dataclasses
from ..shared import action as shared_action
from ..shared import patchedaction as shared_patchedaction
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ActionsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class ActionsPartialUpdateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class ActionsPartialUpdateQueryParams:
    format: Optional[ActionsPartialUpdateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ActionsPartialUpdateRequests:
    patched_action: Optional[shared_patchedaction.PatchedActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_action1: Optional[shared_patchedaction.PatchedActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_action2: Optional[shared_patchedaction.PatchedActionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ActionsPartialUpdateRequest:
    path_params: ActionsPartialUpdatePathParams = dataclasses.field()
    query_params: ActionsPartialUpdateQueryParams = dataclasses.field()
    request: Optional[ActionsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class ActionsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    action: Optional[shared_action.Action] = dataclasses.field(default=None)
    body: Optional[bytes] = dataclasses.field(default=None)
    