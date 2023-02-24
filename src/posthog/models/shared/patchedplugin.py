from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from posthog import utils
from typing import Any, Optional

class PatchedPluginPluginTypeEnum(str, Enum):
    LOCAL = "local"
    CUSTOM = "custom"
    REPOSITORY = "repository"
    SOURCE = "source"
    UNKNOWN = ""
    NULL = "null"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PatchedPluginInput:
    capabilities: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('capabilities'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'capabilities', 'json': True }, 'multipart_form': { 'field_name': 'capabilities', 'json': True }})
    config_schema: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config_schema'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'config_schema', 'json': True }, 'multipart_form': { 'field_name': 'config_schema', 'json': True }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'icon' }, 'multipart_form': { 'field_name': 'icon' }})
    is_global: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_global'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'is_global' }, 'multipart_form': { 'field_name': 'is_global' }})
    metrics: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metrics'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'metrics', 'json': True }, 'multipart_form': { 'field_name': 'metrics', 'json': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    plugin_type: Optional[PatchedPluginPluginTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin_type'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'plugin_type' }, 'multipart_form': { 'field_name': 'plugin_type' }})
    public_jobs: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_jobs'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'public_jobs', 'json': True }, 'multipart_form': { 'field_name': 'public_jobs', 'json': True }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'tag' }, 'multipart_form': { 'field_name': 'tag' }})
    