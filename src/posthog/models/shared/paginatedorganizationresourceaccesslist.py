import dataclasses
from ..shared import organizationresourceaccess as shared_organizationresourceaccess
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PaginatedOrganizationResourceAccessList:
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    next: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next') }})
    previous: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('previous') }})
    results: Optional[list[shared_organizationresourceaccess.OrganizationResourceAccess]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('results') }})
    