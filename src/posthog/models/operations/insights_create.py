from __future__ import annotations
import dataclasses
from ..shared import insight as shared_insight
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsCreateFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsCreateQueryParams:
    format: Optional[InsightsCreateFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsCreateRequest:
    path_params: InsightsCreatePathParams = dataclasses.field()
    query_params: InsightsCreateQueryParams = dataclasses.field()
    request: Optional[shared_insight.InsightInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class InsightsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    insight: Optional[shared_insight.Insight] = dataclasses.field(default=None)
    