from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class HookInput:
    event: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event') }, 'form': { 'field_name': 'event' }, 'multipart_form': { 'field_name': 'event' }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }, 'form': { 'field_name': 'target' }, 'multipart_form': { 'field_name': 'target' }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'id' }, 'multipart_form': { 'field_name': 'id' }})
    resource_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource_id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'resource_id' }, 'multipart_form': { 'field_name': 'resource_id' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Hook:
    created: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    event: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event') }})
    target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target') }})
    team: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('team') }})
    updated: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('id'), 'exclude': lambda f: f is None }})
    resource_id: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource_id'), 'exclude': lambda f: f is None }})
    