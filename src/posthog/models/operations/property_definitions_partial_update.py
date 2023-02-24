from __future__ import annotations
import dataclasses
from ..shared import patchedpropertydefinition as shared_patchedpropertydefinition
from ..shared import propertydefinition as shared_propertydefinition
from typing import Optional


@dataclasses.dataclass
class PropertyDefinitionsPartialUpdatePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class PropertyDefinitionsPartialUpdateRequests:
    patched_property_definition: Optional[shared_patchedpropertydefinition.PatchedPropertyDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_property_definition1: Optional[shared_patchedpropertydefinition.PatchedPropertyDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_property_definition2: Optional[shared_patchedpropertydefinition.PatchedPropertyDefinitionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class PropertyDefinitionsPartialUpdateRequest:
    path_params: PropertyDefinitionsPartialUpdatePathParams = dataclasses.field()
    request: Optional[PropertyDefinitionsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class PropertyDefinitionsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    property_definition: Optional[shared_propertydefinition.PropertyDefinition] = dataclasses.field(default=None)
    