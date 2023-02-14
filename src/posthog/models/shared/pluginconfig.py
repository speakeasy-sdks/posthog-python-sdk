import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class PluginConfigInput:
    order: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }, 'form': { 'field_name': 'order' }, 'multipart_form': { 'field_name': 'order' }})
    plugin: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin') }, 'form': { 'field_name': 'plugin' }, 'multipart_form': { 'field_name': 'plugin' }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }, 'form': { 'field_name': 'enabled' }, 'multipart_form': { 'field_name': 'enabled' }})
    error: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error') }, 'form': { 'field_name': 'error', 'json': True }, 'multipart_form': { 'field_name': 'error', 'json': True }})
    

@dataclass_json
@dataclasses.dataclass
class PluginConfig:
    config: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('config') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    delivery_rate_24h: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('delivery_rate_24h') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    order: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }})
    plugin: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin') }})
    plugin_info: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin_info') }})
    team_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('team_id') }})
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enabled') }})
    error: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('error') }})
    