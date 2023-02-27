from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedOrganizationMemberInput:
    level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('level'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'level' }, 'multipart_form': { 'field_name': 'level' }})
    