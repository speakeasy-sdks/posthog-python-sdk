import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils
from typing import Optional

class PatchedSubscriptionByweekdayEnum(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

class PatchedSubscriptionFrequencyEnum(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class PatchedSubscriptionTargetTypeEnum(str, Enum):
    EMAIL = "email"
    SLACK = "slack"
    WEBHOOK = "webhook"


@dataclass_json
@dataclasses.dataclass
class PatchedSubscriptionInput:
    r"""PatchedSubscriptionInput
    Standard Subscription serializer.
    """
    
    bysetpos: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bysetpos') }, 'form': { 'field_name': 'bysetpos' }, 'multipart_form': { 'field_name': 'bysetpos' }})
    byweekday: Optional[list[PatchedSubscriptionByweekdayEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byweekday') }, 'form': { 'field_name': 'byweekday', 'json': True }, 'multipart_form': { 'field_name': 'byweekday', 'json': True }})
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }, 'form': { 'field_name': 'count' }, 'multipart_form': { 'field_name': 'count' }})
    dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard') }, 'form': { 'field_name': 'dashboard' }, 'multipart_form': { 'field_name': 'dashboard' }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    frequency: Optional[PatchedSubscriptionFrequencyEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency') }, 'form': { 'field_name': 'frequency' }, 'multipart_form': { 'field_name': 'frequency' }})
    insight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('insight') }, 'form': { 'field_name': 'insight' }, 'multipart_form': { 'field_name': 'insight' }})
    interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('interval') }, 'form': { 'field_name': 'interval' }, 'multipart_form': { 'field_name': 'interval' }})
    invite_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invite_message') }, 'form': { 'field_name': 'invite_message' }, 'multipart_form': { 'field_name': 'invite_message' }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }, 'form': { 'field_name': 'start_date' }, 'multipart_form': { 'field_name': 'start_date' }})
    target_type: Optional[PatchedSubscriptionTargetTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_type') }, 'form': { 'field_name': 'target_type' }, 'multipart_form': { 'field_name': 'target_type' }})
    target_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_value') }, 'form': { 'field_name': 'target_value' }, 'multipart_form': { 'field_name': 'target_value' }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('title') }, 'form': { 'field_name': 'title' }, 'multipart_form': { 'field_name': 'title' }})
    until_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('until_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }, 'form': { 'field_name': 'until_date' }, 'multipart_form': { 'field_name': 'until_date' }})
    