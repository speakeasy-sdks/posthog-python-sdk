import dataclasses
from ..shared import hook as shared_hook
from typing import Optional


@dataclasses.dataclass
class HooksUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HooksUpdateRequests:
    hook: Optional[shared_hook.HookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    hook1: Optional[shared_hook.HookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    hook2: Optional[shared_hook.HookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class HooksUpdateRequest:
    path_params: HooksUpdatePathParams = dataclasses.field()
    request: HooksUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class HooksUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    hook: Optional[shared_hook.Hook] = dataclasses.field(default=None)
    