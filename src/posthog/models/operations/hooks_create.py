from __future__ import annotations
import dataclasses
from ..shared import hook as shared_hook
from typing import Optional


@dataclasses.dataclass
class HooksCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HooksCreateRequests:
    hook: Optional[shared_hook.HookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    hook1: Optional[shared_hook.HookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    hook2: Optional[shared_hook.HookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class HooksCreateRequest:
    path_params: HooksCreatePathParams = dataclasses.field()
    request: HooksCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class HooksCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    hook: Optional[shared_hook.Hook] = dataclasses.field(default=None)
    