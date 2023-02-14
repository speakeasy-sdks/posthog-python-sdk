import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PatchedHookInput:
    event: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event') }, 'form': { 'field_name': 'event' }, 'multipart_form': { 'field_name': 'event' }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }, 'form': { 'field_name': 'id' }, 'multipart_form': { 'field_name': 'id' }})
    resource_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource_id') }, 'form': { 'field_name': 'resource_id' }, 'multipart_form': { 'field_name': 'resource_id' }})
    target: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }, 'form': { 'field_name': 'target' }, 'multipart_form': { 'field_name': 'target' }})
    