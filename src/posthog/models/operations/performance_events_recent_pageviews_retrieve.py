import dataclasses
from ..shared import performanceevent as shared_performanceevent
from typing import Optional


@dataclasses.dataclass
class PerformanceEventsRecentPageviewsRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PerformanceEventsRecentPageviewsRetrieveRequest:
    path_params: PerformanceEventsRecentPageviewsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class PerformanceEventsRecentPageviewsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    performance_event: Optional[shared_performanceevent.PerformanceEvent] = dataclasses.field(default=None)
    