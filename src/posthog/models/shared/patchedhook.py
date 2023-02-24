from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedHookInput:
    event: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('event'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'event' }, 'multipart_form': { 'field_name': 'event' }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'id' }, 'multipart_form': { 'field_name': 'id' }})
    resource_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource_id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'resource_id' }, 'multipart_form': { 'field_name': 'resource_id' }})
    target: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'target' }, 'multipart_form': { 'field_name': 'target' }})
    