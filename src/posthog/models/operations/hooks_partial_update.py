from __future__ import annotations
import dataclasses
from ..shared import hook as shared_hook
from ..shared import patchedhook as shared_patchedhook
from typing import Optional


@dataclasses.dataclass
class HooksPartialUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HooksPartialUpdateRequests:
    patched_hook: Optional[shared_patchedhook.PatchedHookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_hook1: Optional[shared_patchedhook.PatchedHookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_hook2: Optional[shared_patchedhook.PatchedHookInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class HooksPartialUpdateRequest:
    path_params: HooksPartialUpdatePathParams = dataclasses.field()
    request: Optional[HooksPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class HooksPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    hook: Optional[shared_hook.Hook] = dataclasses.field(default=None)
    