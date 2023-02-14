import dataclasses
from ..shared import clickhouseevent as shared_clickhouseevent
from enum import Enum
from typing import Optional


@dataclasses.dataclass
class EventsRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    
class EventsRetrieveFormatEnum(str, Enum):
    CSV = "csv"
    JSON = "json"


@dataclasses.dataclass
class EventsRetrieveQueryParams:
    format: Optional[EventsRetrieveFormatEnum] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'format', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class EventsRetrieveRequest:
    path_params: EventsRetrievePathParams = dataclasses.field()
    query_params: EventsRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class EventsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    body: Optional[bytes] = dataclasses.field(default=None)
    clickhouse_event: Optional[shared_clickhouseevent.ClickhouseEvent] = dataclasses.field(default=None)
    