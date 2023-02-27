from __future__ import annotations
import dataclasses
from ..shared import trend as shared_trend
from ..shared import trendresults as shared_trendresults
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class TrendsPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class TrendsFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class TrendsQueryParams:
    format: Optional[TrendsFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class TrendsRequest:
    path_params: TrendsPathParams = dataclasses.field()
    query_params: TrendsQueryParams = dataclasses.field()
    request: Optional[shared_trend.Trend] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class TrendsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    trend_results: Optional[shared_trendresults.TrendResults] = dataclasses.field(default=None)
    