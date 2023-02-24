from __future__ import annotations
import dataclasses
from ..shared import filteraction as shared_filteraction
from ..shared import filterevent as shared_filterevent
from ..shared import funnelexclusion as shared_funnelexclusion
from ..shared import property as shared_property
from dataclasses_json import Undefined, dataclass_json
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


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Funnel:
    actions: Optional[list[shared_filteraction.FilterAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions'), 'exclude': lambda f: f is None }})
    aggregation_group_type_index: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('aggregation_group_type_index'), 'exclude': lambda f: f is None }})
    breakdown: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown'), 'exclude': lambda f: f is None }})
    breakdown_limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown_limit'), 'exclude': lambda f: f is None }})
    breakdown_type: Optional[FunnelBreakdownTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown_type'), 'exclude': lambda f: f is None }})
    date_from: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_from'), 'exclude': lambda f: f is None }})
    date_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_to'), 'exclude': lambda f: f is None }})
    events: Optional[list[shared_filterevent.FilterEvent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('events'), 'exclude': lambda f: f is None }})
    exclusions: Optional[list[shared_funnelexclusion.FunnelExclusion]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('exclusions'), 'exclude': lambda f: f is None }})
    filter_test_accounts: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter_test_accounts'), 'exclude': lambda f: f is None }})
    funnel_order_type: Optional[FunnelFunnelOrderTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_order_type'), 'exclude': lambda f: f is None }})
    funnel_viz_type: Optional[FunnelFunnelVizTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_viz_type'), 'exclude': lambda f: f is None }})
    funnel_window_days: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_window_days'), 'exclude': lambda f: f is None }})
    funnel_window_interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_window_interval'), 'exclude': lambda f: f is None }})
    funnel_window_interval_type: Optional[FunnelFunnelWindowIntervalTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('funnel_window_interval_type'), 'exclude': lambda f: f is None }})
    properties: Optional[shared_property.Property] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties'), 'exclude': lambda f: f is None }})
    