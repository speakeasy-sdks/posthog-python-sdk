from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class FunnelStepsResult:
    action_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_id') }})
    average_conversion_time: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('average_conversion_time') }})
    converted_people_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('converted_people_url') }})
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    dropped_people_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dropped_people_url') }})
    median_conversion_time: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('median_conversion_time') }})
    order: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }})
    