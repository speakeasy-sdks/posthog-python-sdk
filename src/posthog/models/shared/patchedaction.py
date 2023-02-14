import dataclasses
import dateutil.parser
from ..shared import actionstep as shared_actionstep
from dataclasses_json import dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class PatchedActionInput:
    r"""PatchedActionInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    last_calculated_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_calculated_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }, 'form': { 'field_name': 'last_calculated_at' }, 'multipart_form': { 'field_name': 'last_calculated_at' }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    post_to_slack: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('post_to_slack') }, 'form': { 'field_name': 'post_to_slack' }, 'multipart_form': { 'field_name': 'post_to_slack' }})
    slack_message_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('slack_message_format') }, 'form': { 'field_name': 'slack_message_format' }, 'multipart_form': { 'field_name': 'slack_message_format' }})
    steps: Optional[list[shared_actionstep.ActionStep]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('steps') }, 'form': { 'field_name': 'steps', 'json': True }, 'multipart_form': { 'field_name': 'steps', 'json': True }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }, 'form': { 'field_name': 'tags', 'json': True }, 'multipart_form': { 'field_name': 'tags', 'json': True }})
    