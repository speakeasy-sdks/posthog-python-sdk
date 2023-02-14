import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PatchedRoleInput:
    feature_flags_access_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flags_access_level') }, 'form': { 'field_name': 'feature_flags_access_level' }, 'multipart_form': { 'field_name': 'feature_flags_access_level' }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    