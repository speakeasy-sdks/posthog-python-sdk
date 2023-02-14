import dataclasses
from ..shared import insight as shared_insight
from ..shared import patchedinsight as shared_patchedinsight
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsPartialUpdateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsPartialUpdateQueryParams:
    format: Optional[InsightsPartialUpdateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsPartialUpdateRequest:
    path_params: InsightsPartialUpdatePathParams = dataclasses.field()
    query_params: InsightsPartialUpdateQueryParams = dataclasses.field()
    request: Optional[shared_patchedinsight.PatchedInsightInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class InsightsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    insight: Optional[shared_insight.Insight] = dataclasses.field(default=None)
    