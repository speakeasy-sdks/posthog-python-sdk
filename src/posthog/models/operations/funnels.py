import dataclasses
from ..shared import funnel as shared_funnel
from ..shared import funnelstepsresults as shared_funnelstepsresults
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class FunnelsPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class FunnelsFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class FunnelsQueryParams:
    format: Optional[FunnelsFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class FunnelsRequest:
    path_params: FunnelsPathParams = dataclasses.field()
    query_params: FunnelsQueryParams = dataclasses.field()
    request: Optional[shared_funnel.Funnel] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class FunnelsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    funnel_steps_results: Optional[shared_funnelstepsresults.FunnelStepsResults] = dataclasses.field(default=None)
    