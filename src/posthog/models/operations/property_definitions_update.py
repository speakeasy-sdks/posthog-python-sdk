import dataclasses
from ..shared import propertydefinition as shared_propertydefinition
from typing import Optional


@dataclasses.dataclass
class PropertyDefinitionsUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PropertyDefinitionsUpdateRequests:
    property_definition: Optional[shared_propertydefinition.PropertyDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    property_definition1: Optional[shared_propertydefinition.PropertyDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    property_definition2: Optional[shared_propertydefinition.PropertyDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PropertyDefinitionsUpdateRequest:
    path_params: PropertyDefinitionsUpdatePathParams = dataclasses.field()
    request: PropertyDefinitionsUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class PropertyDefinitionsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    property_definition: Optional[shared_propertydefinition.PropertyDefinition] = dataclasses.field(default=None)
    