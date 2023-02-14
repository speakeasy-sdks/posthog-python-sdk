import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils


@dataclass_json
@dataclasses.dataclass
class ClickhouseEvent:
    distinct_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id') }})
    elements: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('elements') }})
    elements_chain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('elements_chain') }})
    event: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    person: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('person') }})
    properties: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties') }})
    timestamp: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('timestamp') }})
    