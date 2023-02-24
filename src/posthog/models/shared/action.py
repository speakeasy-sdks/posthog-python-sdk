from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import actionstep as shared_actionstep
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActionInput:
    r"""ActionInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    last_calculated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_calculated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'last_calculated_at' }, 'multipart_form': { 'field_name': 'last_calculated_at' }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    post_to_slack: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('post_to_slack'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'post_to_slack' }, 'multipart_form': { 'field_name': 'post_to_slack' }})
    slack_message_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slack_message_format'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'slack_message_format' }, 'multipart_form': { 'field_name': 'slack_message_format' }})
    steps: Optional[list[shared_actionstep.ActionStep]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('steps'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'steps', 'json': True }, 'multipart_form': { 'field_name': 'steps', 'json': True }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'tags' }, 'multipart_form': { 'field_name': 'tags' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActionCreatedBy:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    distinct_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id'), 'exclude': lambda f: f is None }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Action:
    r"""Action
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: ActionCreatedBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_action: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_action') }})
    is_calculating: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_calculating') }})
    team_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('team_id') }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    last_calculated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_calculated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    post_to_slack: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('post_to_slack'), 'exclude': lambda f: f is None }})
    slack_message_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slack_message_format'), 'exclude': lambda f: f is None }})
    steps: Optional[list[shared_actionstep.ActionStep]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('steps'), 'exclude': lambda f: f is None }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags'), 'exclude': lambda f: f is None }})
    