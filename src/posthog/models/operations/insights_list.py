from __future__ import annotations
import dataclasses
from ..shared import paginatedinsightlist as shared_paginatedinsightlist
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsListFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsListQueryParams:
    created_by: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created_by', 'style': 'form', 'explode': True }})
    format: Optional[InsightsListFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    short_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'short_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsListRequest:
    path_params: InsightsListPathParams = dataclasses.field()
    query_params: InsightsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class InsightsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    paginated_insight_list: Optional[shared_paginatedinsightlist.PaginatedInsightList] = dataclasses.field(default=None)
    