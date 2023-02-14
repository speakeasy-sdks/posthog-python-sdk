import dataclasses
from ..shared import eventdefinition as shared_eventdefinition
from typing import Optional


@dataclasses.dataclass
class EventDefinitionsUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class EventDefinitionsUpdateRequests:
    event_definition: Optional[shared_eventdefinition.EventDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    event_definition1: Optional[shared_eventdefinition.EventDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    event_definition2: Optional[shared_eventdefinition.EventDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class EventDefinitionsUpdateRequest:
    path_params: EventDefinitionsUpdatePathParams = dataclasses.field()
    request: EventDefinitionsUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class EventDefinitionsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    event_definition: Optional[shared_eventdefinition.EventDefinition] = dataclasses.field(default=None)
    