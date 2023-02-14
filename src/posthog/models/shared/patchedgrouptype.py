import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PatchedGroupTypeInput:
    name_plural: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name_plural') }, 'form': { 'field_name': 'name_plural' }, 'multipart_form': { 'field_name': 'name_plural' }})
    name_singular: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name_singular') }, 'form': { 'field_name': 'name_singular' }, 'multipart_form': { 'field_name': 'name_singular' }})
    