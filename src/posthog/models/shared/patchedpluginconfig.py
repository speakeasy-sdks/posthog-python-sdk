from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedPluginConfigInput:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'enabled' }, 'multipart_form': { 'field_name': 'enabled' }})
    error: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'error', 'json': True }, 'multipart_form': { 'field_name': 'error', 'json': True }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'order' }, 'multipart_form': { 'field_name': 'order' }})
    plugin: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'plugin' }, 'multipart_form': { 'field_name': 'plugin' }})
    