import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PatchedOrganizationMemberInput:
    level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('level') }, 'form': { 'field_name': 'level' }, 'multipart_form': { 'field_name': 'level' }})
    