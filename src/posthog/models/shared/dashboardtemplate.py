import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils


@dataclass_json
@dataclasses.dataclass
class DashboardTemplate:
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('url') }, 'form': { 'field_name': 'url' }, 'multipart_form': { 'field_name': 'url' }})
    