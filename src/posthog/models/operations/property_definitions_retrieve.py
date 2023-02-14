import dataclasses
from ..shared import propertydefinition as shared_propertydefinition
from typing import Optional


@dataclasses.dataclass
class PropertyDefinitionsRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PropertyDefinitionsRetrieveRequest:
    path_params: PropertyDefinitionsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class PropertyDefinitionsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    property_definition: Optional[shared_propertydefinition.PropertyDefinition] = dataclasses.field(default=None)
    