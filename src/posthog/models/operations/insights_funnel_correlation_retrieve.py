import dataclasses
from ..shared import insight as shared_insight
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsFunnelCorrelationRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsFunnelCorrelationRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsFunnelCorrelationRetrieveQueryParams:
    format: Optional[InsightsFunnelCorrelationRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsFunnelCorrelationRetrieveRequest:
    path_params: InsightsFunnelCorrelationRetrievePathParams = dataclasses.field()
    query_params: InsightsFunnelCorrelationRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class InsightsFunnelCorrelationRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    insight: Optional[shared_insight.Insight] = dataclasses.field(default=None)
    