import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Optional

class PropertyItemOperatorEnum(str, Enum):
    EXACT = "exact"
    IS_NOT = "is_not"
    ICONTAINS = "icontains"
    NOT_ICONTAINS = "not_icontains"
    REGEX = "regex"
    NOT_REGEX = "not_regex"
    GT = "gt"
    LT = "lt"
    GTE = "gte"
    LTE = "lte"
    IS_SET = "is_set"
    IS_NOT_SET = "is_not_set"
    IS_DATE_EXACT = "is_date_exact"
    IS_DATE_AFTER = "is_date_after"
    IS_DATE_BEFORE = "is_date_before"
    UNKNOWN = ""
    NULL = "null"

class PropertyItemTypeEnum(str, Enum):
    EVENT = "event"
    PERSON = "person"
    COHORT = "cohort"
    ELEMENT = "element"
    STATIC_COHORT = "static-cohort"
    PRECALCULATED_COHORT = "precalculated-cohort"
    GROUP = "group"
    RECORDING = "recording"
    BEHAVIORAL = "behavioral"
    SESSION = "session"
    HOGQL = "hogql"
    UNKNOWN = ""


@dataclass_json
@dataclasses.dataclass
class PropertyItem:
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    operator: Optional[PropertyItemOperatorEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('operator') }})
    type: Optional[PropertyItemTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    