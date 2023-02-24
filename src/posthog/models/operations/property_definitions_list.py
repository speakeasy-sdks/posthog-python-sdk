from __future__ import annotations
import dataclasses
from ..shared import paginatedpropertydefinitionlist as shared_paginatedpropertydefinitionlist
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class PropertyDefinitionsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class PropertyDefinitionsListTypeEnum(str, Enum):
    EVENT = "event"
    PERSON = "person"
    GROUP = "group"


@dataclasses.dataclass
class PropertyDefinitionsListQueryParams:
    event_names: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event_names', 'style': 'form', 'explode': True }})
    excluded_properties: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'excluded_properties', 'style': 'form', 'explode': True }})
    filter_by_event_names: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'filter_by_event_names', 'style': 'form', 'explode': True }})
    group_type_index: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'group_type_index', 'style': 'form', 'explode': True }})
    is_feature_flag: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'is_feature_flag', 'style': 'form', 'explode': True }})
    is_numerical: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'is_numerical', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    properties: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'properties', 'style': 'form', 'explode': True }})
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    type: Optional[PropertyDefinitionsListTypeEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'type', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class PropertyDefinitionsListRequest:
    path_params: PropertyDefinitionsListPathParams = dataclasses.field()
    query_params: PropertyDefinitionsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class PropertyDefinitionsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_property_definition_list: Optional[shared_paginatedpropertydefinitionlist.PaginatedPropertyDefinitionList] = dataclasses.field(default=None)
    