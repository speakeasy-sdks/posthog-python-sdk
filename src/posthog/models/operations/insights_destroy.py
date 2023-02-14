import dataclasses
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class InsightsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class InsightsDestroyFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class InsightsDestroyQueryParams:
    format: Optional[InsightsDestroyFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class InsightsDestroyRequest:
    path_params: InsightsDestroyPathParams = dataclasses.field()
    query_params: InsightsDestroyQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class InsightsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    