import dataclasses
from dataclasses_json import dataclass_json
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


@dataclass_json
@dataclasses.dataclass
class PatchedOrganizationResourceAccessInput:
    access_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('access_level') }, 'form': { 'field_name': 'access_level' }, 'multipart_form': { 'field_name': 'access_level' }})
    resource: Optional[PatchedOrganizationResourceAccessResourceEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource') }, 'form': { 'field_name': 'resource' }, 'multipart_form': { 'field_name': 'resource' }})
    