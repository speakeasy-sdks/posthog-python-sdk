from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils

class PluginLogEntrySourceEnum(str, Enum):
    SYSTEM = "SYSTEM"
    PLUGIN = "PLUGIN"
    CONSOLE = "CONSOLE"

class PluginLogEntryTypeEnum(str, Enum):
    DEBUG = "DEBUG"
    LOG = "LOG"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PluginLogEntry:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    instance_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('instance_id') }})
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('message') }})
    plugin_config_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin_config_id') }})
    plugin_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plugin_id') }})
    source: PluginLogEntrySourceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    team_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('team_id') }})
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    type: PluginLogEntryTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    