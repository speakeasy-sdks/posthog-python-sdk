import dataclasses
from ..shared import eventdefinition as shared_eventdefinition
from typing import Optional


@dataclasses.dataclass
class EventDefinitionsRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class EventDefinitionsRetrieveRequest:
    path_params: EventDefinitionsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class EventDefinitionsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    event_definition: Optional[shared_eventdefinition.EventDefinition] = dataclasses.field(default=None)
    