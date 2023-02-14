import dataclasses
from ..shared import property as shared_property
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Optional

class FilterEventMathEnum(str, Enum):
    TOTAL = "total"
    DAU = "dau"
    WEEKLY_ACTIVE = "weekly_active"
    MONTHLY_ACTIVE = "monthly_active"
    UNIQUE_GROUP = "unique_group"
    UNIQUE_SESSION = "unique_session"
    SUM = "sum"
    MIN = "min"
    MAX = "max"
    AVG = "avg"
    MEDIAN = "median"
    P90 = "p90"
    P95 = "p95"
    P99 = "p99"
    MIN_COUNT_PER_ACTOR = "min_count_per_actor"
    MAX_COUNT_PER_ACTOR = "max_count_per_actor"
    AVG_COUNT_PER_ACTOR = "avg_count_per_actor"
    MEDIAN_COUNT_PER_ACTOR = "median_count_per_actor"
    P90_COUNT_PER_ACTOR = "p90_count_per_actor"
    P95_COUNT_PER_ACTOR = "p95_count_per_actor"
    P99_COUNT_PER_ACTOR = "p99_count_per_actor"


@dataclass_json
@dataclasses.dataclass
class FilterEvent:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    math: Optional[FilterEventMathEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('math') }})
    properties: Optional[list[shared_property.Property]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties') }})
    