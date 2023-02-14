import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils


@dataclass_json
@dataclasses.dataclass
class TaggedItem:
    tag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag') }})
    