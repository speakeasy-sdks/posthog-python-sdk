from __future__ import annotations
import dataclasses
from ..shared import paginatedactionlist as shared_paginatedactionlist
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class ActionsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class ActionsListFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class ActionsListQueryParams:
    format: Optional[ActionsListFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ActionsListRequest:
    path_params: ActionsListPathParams = dataclasses.field()
    query_params: ActionsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ActionsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    paginated_action_list: Optional[shared_paginatedactionlist.PaginatedActionList] = dataclasses.field(default=None)
    