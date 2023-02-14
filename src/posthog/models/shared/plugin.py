import dataclasses
from dataclasses_json import dataclass_json
from enum import Enum
from posthog import utils
from typing import Any, Optional

class PluginPluginTypeEnum(str, Enum):
    LOCAL = "local"
    CUSTOM = "custom"
    REPOSITORY = "repository"
    SOURCE = "source"
    UNKNOWN = ""
    NULL = "null"


@dataclass_json
@dataclasses.dataclass
class PluginInput:
    capabilities: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('capabilities') }, 'form': { 'field_name': 'capabilities', 'json': True }, 'multipart_form': { 'field_name': 'capabilities', 'json': True }})
    config_schema: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config_schema') }, 'form': { 'field_name': 'config_schema', 'json': True }, 'multipart_form': { 'field_name': 'config_schema', 'json': True }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }, 'form': { 'field_name': 'icon' }, 'multipart_form': { 'field_name': 'icon' }})
    is_global: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_global') }, 'form': { 'field_name': 'is_global' }, 'multipart_form': { 'field_name': 'is_global' }})
    metrics: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metrics') }, 'form': { 'field_name': 'metrics', 'json': True }, 'multipart_form': { 'field_name': 'metrics', 'json': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    plugin_type: Optional[PluginPluginTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin_type') }, 'form': { 'field_name': 'plugin_type' }, 'multipart_form': { 'field_name': 'plugin_type' }})
    public_jobs: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_jobs') }, 'form': { 'field_name': 'public_jobs', 'json': True }, 'multipart_form': { 'field_name': 'public_jobs', 'json': True }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag') }, 'form': { 'field_name': 'tag' }, 'multipart_form': { 'field_name': 'tag' }})
    

@dataclass_json
@dataclasses.dataclass
class Plugin:
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    latest_tag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('latest_tag') }})
    organization_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('organization_id') }})
    organization_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('organization_name') }})
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('url') }})
    capabilities: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('capabilities') }})
    config_schema: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config_schema') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    is_global: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_global') }})
    metrics: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('metrics') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    plugin_type: Optional[PluginPluginTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin_type') }})
    public_jobs: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_jobs') }})
    tag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag') }})
    