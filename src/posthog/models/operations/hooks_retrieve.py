import dataclasses
from ..shared import hook as shared_hook
from typing import Optional


@dataclasses.dataclass
class HooksRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HooksRetrieveRequest:
    path_params: HooksRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class HooksRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    hook: Optional[shared_hook.Hook] = dataclasses.field(default=None)
    