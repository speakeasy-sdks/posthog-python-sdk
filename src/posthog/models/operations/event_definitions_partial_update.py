from __future__ import annotations
import dataclasses
from ..shared import eventdefinition as shared_eventdefinition
from ..shared import patchedeventdefinition as shared_patchedeventdefinition
from typing import Optional


@dataclasses.dataclass
class EventDefinitionsPartialUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class EventDefinitionsPartialUpdateRequests:
    patched_event_definition: Optional[shared_patchedeventdefinition.PatchedEventDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_event_definition1: Optional[shared_patchedeventdefinition.PatchedEventDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_event_definition2: Optional[shared_patchedeventdefinition.PatchedEventDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class EventDefinitionsPartialUpdateRequest:
    path_params: EventDefinitionsPartialUpdatePathParams = dataclasses.field()
    request: Optional[EventDefinitionsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class EventDefinitionsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    event_definition: Optional[shared_eventdefinition.EventDefinition] = dataclasses.field(default=None)
    