from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DashboardTileBasic:
    dashboard_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard_id') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }})
    