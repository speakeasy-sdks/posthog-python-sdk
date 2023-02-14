import dataclasses
from ..shared import featureflagroleaccess as shared_featureflagroleaccess
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PaginatedFeatureFlagRoleAccessList:
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    next: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next') }})
    previous: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous') }})
    results: Optional[list[shared_featureflagroleaccess.FeatureFlagRoleAccessOutput]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    