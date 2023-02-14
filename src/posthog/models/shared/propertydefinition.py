import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Any, Optional

class PropertyDefinitionPropertyTypeEnum(str, Enum):
    DATE_TIME = "DateTime"
    STRING = "String"
    NUMERIC = "Numeric"
    BOOLEAN = "Boolean"
    UNKNOWN = ""
    NULL = "null"


@dataclass_json
@dataclasses.dataclass
class PropertyDefinitionInput:
    r"""PropertyDefinitionInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    is_numerical: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_numerical') }, 'form': { 'field_name': 'is_numerical' }, 'multipart_form': { 'field_name': 'is_numerical' }})
    property_type: Optional[PropertyDefinitionPropertyTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property_type') }, 'form': { 'field_name': 'property_type' }, 'multipart_form': { 'field_name': 'property_type' }})
    query_usage_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('query_usage_30_day') }, 'form': { 'field_name': 'query_usage_30_day' }, 'multipart_form': { 'field_name': 'query_usage_30_day' }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }, 'form': { 'field_name': 'tags', 'json': True }, 'multipart_form': { 'field_name': 'tags', 'json': True }})
    

@dataclass_json
@dataclasses.dataclass
class PropertyDefinition:
    r"""PropertyDefinition
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_seen_on_filtered_events: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_seen_on_filtered_events') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    is_numerical: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_numerical') }})
    property_type: Optional[PropertyDefinitionPropertyTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property_type') }})
    query_usage_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('query_usage_30_day') }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }})
    