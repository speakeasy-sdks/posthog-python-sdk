from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from posthog import utils
from typing import Optional

class PatchedOrganizationResourceAccessResourceEnum(str, Enum):
    FEATURE_FLAGS = "feature flags"
    EXPERIMENTS = "experiments"
    COHORTS = "cohorts"
    DATA_MANAGEMENT = "data management"
    SESSION_RECORDINGS = "session recordings"
    INSIGHTS = "insights"
    DASHBOARDS = "dashboards"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedOrganizationResourceAccessInput:
    access_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('access_level'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'access_level' }, 'multipart_form': { 'field_name': 'access_level' }})
    resource: Optional[PatchedOrganizationResourceAccessResourceEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'resource' }, 'multipart_form': { 'field_name': 'resource' }})
    