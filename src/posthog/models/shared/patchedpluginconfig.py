import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class PatchedPluginConfigInput:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }, 'form': { 'field_name': 'enabled' }, 'multipart_form': { 'field_name': 'enabled' }})
    error: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error') }, 'form': { 'field_name': 'error', 'json': True }, 'multipart_form': { 'field_name': 'error', 'json': True }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }, 'form': { 'field_name': 'order' }, 'multipart_form': { 'field_name': 'order' }})
    plugin: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin') }, 'form': { 'field_name': 'plugin' }, 'multipart_form': { 'field_name': 'plugin' }})
    