from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GroupType:
    group_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('group_type') }})
    group_type_index: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('group_type_index') }})
    name_plural: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name_plural'), 'exclude': lambda f: f is None }})
    name_singular: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name_singular'), 'exclude': lambda f: f is None }})
    