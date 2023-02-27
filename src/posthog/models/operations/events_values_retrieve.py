from __future__ import annotations
import dataclasses
from ..shared import clickhouseevent as shared_clickhouseevent
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class EventsValuesRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class EventsValuesRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class EventsValuesRetrieveQueryParams:
    format: Optional[EventsValuesRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class EventsValuesRetrieveRequest:
    path_params: EventsValuesRetrievePathParams = dataclasses.field()
    query_params: EventsValuesRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class EventsValuesRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    clickhouse_event: Optional[shared_clickhouseevent.ClickhouseEvent] = dataclasses.field(default=None)
    