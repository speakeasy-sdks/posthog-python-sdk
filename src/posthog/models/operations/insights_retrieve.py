from __future__ import annotations
import dataclasses
from ..shared import insight as shared_insight
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsRetrieveQueryParams:
    format: Optional[InsightsRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    from_dashboard: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'from_dashboard', 'style': 'form', 'explode': True }})
    refresh: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'refresh', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsRetrieveRequest:
    path_params: InsightsRetrievePathParams = dataclasses.field()
    query_params: InsightsRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class InsightsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    insight: Optional[shared_insight.Insight] = dataclasses.field(default=None)
    