from __future__ import annotations
import dataclasses
from ..shared import insight as shared_insight
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsMyLastViewedRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsMyLastViewedRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsMyLastViewedRetrieveQueryParams:
    format: Optional[InsightsMyLastViewedRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsMyLastViewedRetrieveRequest:
    path_params: InsightsMyLastViewedRetrievePathParams = dataclasses.field()
    query_params: InsightsMyLastViewedRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class InsightsMyLastViewedRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    insight: Optional[shared_insight.Insight] = dataclasses.field(default=None)
    