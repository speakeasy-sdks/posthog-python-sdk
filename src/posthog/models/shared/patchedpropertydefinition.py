import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Any, Optional

class PatchedPropertyDefinitionPropertyTypeEnum(str, Enum):
    DATE_TIME = "DateTime"
    STRING = "String"
    NUMERIC = "Numeric"
    BOOLEAN = "Boolean"
    UNKNOWN = ""
    NULL = "null"


@dataclass_json
@dataclasses.dataclass
class PatchedPropertyDefinitionInput:
    r"""PatchedPropertyDefinitionInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    is_numerical: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_numerical') }, 'form': { 'field_name': 'is_numerical' }, 'multipart_form': { 'field_name': 'is_numerical' }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    property_type: Optional[PatchedPropertyDefinitionPropertyTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('property_type') }, 'form': { 'field_name': 'property_type' }, 'multipart_form': { 'field_name': 'property_type' }})
    query_usage_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('query_usage_30_day') }, 'form': { 'field_name': 'query_usage_30_day' }, 'multipart_form': { 'field_name': 'query_usage_30_day' }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }, 'form': { 'field_name': 'tags', 'json': True }, 'multipart_form': { 'field_name': 'tags', 'json': True }})
    