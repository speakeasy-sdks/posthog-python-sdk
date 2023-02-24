from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventDefinitionInput:
    r"""EventDefinitionInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'created_at' }, 'multipart_form': { 'field_name': 'created_at' }})
    last_seen_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_seen_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'last_seen_at' }, 'multipart_form': { 'field_name': 'last_seen_at' }})
    post_to_slack: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('post_to_slack'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'post_to_slack' }, 'multipart_form': { 'field_name': 'post_to_slack' }})
    query_usage_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('query_usage_30_day'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'query_usage_30_day' }, 'multipart_form': { 'field_name': 'query_usage_30_day' }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'tags' }, 'multipart_form': { 'field_name': 'tags' }})
    volume_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('volume_30_day'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'volume_30_day' }, 'multipart_form': { 'field_name': 'volume_30_day' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventDefinitionCreatedBy:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    distinct_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id'), 'exclude': lambda f: f is None }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EventDefinition:
    r"""EventDefinition
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    action_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('action_id') }})
    created_by: EventDefinitionCreatedBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_action: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_action') }})
    is_calculating: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_calculating') }})
    last_calculated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_calculated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    last_updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    last_seen_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_seen_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    post_to_slack: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('post_to_slack'), 'exclude': lambda f: f is None }})
    query_usage_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('query_usage_30_day'), 'exclude': lambda f: f is None }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags'), 'exclude': lambda f: f is None }})
    volume_30_day: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('volume_30_day'), 'exclude': lambda f: f is None }})
    