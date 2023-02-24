from __future__ import annotations
import dataclasses
from ..shared import propertyitem as shared_propertyitem
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from posthog import utils
from typing import Optional

class PropertyTypeEnum(str, Enum):
    AND = "AND"
    OR = "OR"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Property:
    values: list[shared_propertyitem.PropertyItem] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('values') }})
    type: Optional[PropertyTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type'), 'exclude': lambda f: f is None }})
    