from __future__ import annotations
import dataclasses
from ..shared import paginatedeventdefinitionlist as shared_paginatedeventdefinitionlist
from typing import Optional


@dataclasses.dataclass
class EventDefinitionsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class EventDefinitionsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class EventDefinitionsListRequest:
    path_params: EventDefinitionsListPathParams = dataclasses.field()
    query_params: EventDefinitionsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class EventDefinitionsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_event_definition_list: Optional[shared_paginatedeventdefinitionlist.PaginatedEventDefinitionList] = dataclasses.field(default=None)
    