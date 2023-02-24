from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedDashboardInput:
    r"""PatchedDashboardInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    delete_insights: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('delete_insights'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'delete_insights' }, 'multipart_form': { 'field_name': 'delete_insights' }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'filters', 'json': True }, 'multipart_form': { 'field_name': 'filters', 'json': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    pinned: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pinned'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'pinned' }, 'multipart_form': { 'field_name': 'pinned' }})
    restriction_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('restriction_level'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'restriction_level' }, 'multipart_form': { 'field_name': 'restriction_level' }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'tags' }, 'multipart_form': { 'field_name': 'tags' }})
    use_dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_dashboard'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'use_dashboard' }, 'multipart_form': { 'field_name': 'use_dashboard' }})
    use_template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_template'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'use_template' }, 'multipart_form': { 'field_name': 'use_template' }})
    