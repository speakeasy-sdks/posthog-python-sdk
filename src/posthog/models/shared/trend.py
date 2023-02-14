import dataclasses
from ..shared import filteraction as shared_filteraction
from ..shared import filterevent as shared_filterevent
from ..shared import property as shared_property
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Optional

class TrendBreakdownTypeEnum(str, Enum):
    EVENT = "event"
    PERSON = "person"
    COHORT = "cohort"
    GROUP = "group"
    SESSION = "session"
    HOGQL = "hogql"

class TrendDisplayEnum(str, Enum):
    ACTIONS_LINE_GRAPH = "ActionsLineGraph"
    ACTIONS_LINE_GRAPH_CUMULATIVE = "ActionsLineGraphCumulative"
    ACTIONS_TABLE = "ActionsTable"
    ACTIONS_PIE = "ActionsPie"
    ACTIONS_BAR = "ActionsBar"
    ACTIONS_BAR_VALUE = "ActionsBarValue"
    WORLD_MAP = "WorldMap"
    BOLD_NUMBER = "BoldNumber"


@dataclass_json
@dataclasses.dataclass
class Trend:
    actions: Optional[list[shared_filteraction.FilterAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions') }})
    breakdown: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown') }})
    breakdown_type: Optional[TrendBreakdownTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('breakdown_type') }})
    compare: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('compare') }})
    date_from: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_from') }})
    date_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_to') }})
    display: Optional[TrendDisplayEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('display') }})
    events: Optional[list[shared_filterevent.FilterEvent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('events') }})
    filter_test_accounts: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter_test_accounts') }})
    formula: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('formula') }})
    properties: Optional[shared_property.Property] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties') }})
    