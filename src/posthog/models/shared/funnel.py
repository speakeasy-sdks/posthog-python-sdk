import dataclasses
from ..shared import filteraction as shared_filteraction
from ..shared import filterevent as shared_filterevent
from ..shared import funnelexclusion as shared_funnelexclusion
from ..shared import property as shared_property
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Optional

class FunnelBreakdownTypeEnum(str, Enum):
    EVENT = "event"
    PERSON = "person"
    COHORT = "cohort"
    GROUP = "group"
    SESSION = "session"
    HOGQL = "hogql"

class FunnelFunnelOrderTypeEnum(str, Enum):
    STRICT = "strict"
    UNORDERED = "unordered"
    ORDERED = "ordered"

class FunnelFunnelVizTypeEnum(str, Enum):
    TRENDS = "trends"
    TIME_TO_CONVERT = "time_to_convert"
    STEPS = "steps"

class FunnelFunnelWindowIntervalTypeEnum(str, Enum):
    DAY = "DAY"
    MINUTE = "MINUTE"
    HOUR = "HOUR"
    WEEK = "WEEK"
    MONTH = "MONTH"


@dataclass_json
@dataclasses.dataclass
class Funnel:
    actions: Optional[list[shared_filteraction.FilterAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions') }})
    aggregation_group_type_index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('aggregation_group_type_index') }})
    breakdown: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown') }})
    breakdown_limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown_limit') }})
    breakdown_type: Optional[FunnelBreakdownTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown_type') }})
    date_from: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_from') }})
    date_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_to') }})
    events: Optional[list[shared_filterevent.FilterEvent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('events') }})
    exclusions: Optional[list[shared_funnelexclusion.FunnelExclusion]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('exclusions') }})
    filter_test_accounts: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter_test_accounts') }})
    funnel_order_type: Optional[FunnelFunnelOrderTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_order_type') }})
    funnel_viz_type: Optional[FunnelFunnelVizTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_viz_type') }})
    funnel_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_window_days') }})
    funnel_window_interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_window_interval') }})
    funnel_window_interval_type: Optional[FunnelFunnelWindowIntervalTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_window_interval_type') }})
    properties: Optional[shared_property.Property] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties') }})
    