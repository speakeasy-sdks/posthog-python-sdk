from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils
from typing import Optional

class SubscriptionByweekdayEnum(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

class SubscriptionFrequencyEnum(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

class SubscriptionTargetTypeEnum(str, Enum):
    EMAIL = "email"
    SLACK = "slack"
    WEBHOOK = "webhook"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionInput:
    r"""SubscriptionInput
    Standard Subscription serializer.
    """
    
    frequency: SubscriptionFrequencyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency') }, 'form': { 'field_name': 'frequency' }, 'multipart_form': { 'field_name': 'frequency' }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }, 'form': { 'field_name': 'start_date' }, 'multipart_form': { 'field_name': 'start_date' }})
    target_type: SubscriptionTargetTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_type') }, 'form': { 'field_name': 'target_type' }, 'multipart_form': { 'field_name': 'target_type' }})
    target_value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_value') }, 'form': { 'field_name': 'target_value' }, 'multipart_form': { 'field_name': 'target_value' }})
    bysetpos: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bysetpos'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'bysetpos' }, 'multipart_form': { 'field_name': 'bysetpos' }})
    byweekday: Optional[list[SubscriptionByweekdayEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byweekday'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'byweekday' }, 'multipart_form': { 'field_name': 'byweekday' }})
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'count' }, 'multipart_form': { 'field_name': 'count' }})
    dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'dashboard' }, 'multipart_form': { 'field_name': 'dashboard' }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    insight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('insight'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'insight' }, 'multipart_form': { 'field_name': 'insight' }})
    interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('interval'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'interval' }, 'multipart_form': { 'field_name': 'interval' }})
    invite_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invite_message'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'invite_message' }, 'multipart_form': { 'field_name': 'invite_message' }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('title'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'title' }, 'multipart_form': { 'field_name': 'title' }})
    until_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('until_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'until_date' }, 'multipart_form': { 'field_name': 'until_date' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubscriptionCreatedBy:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    distinct_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id'), 'exclude': lambda f: f is None }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Subscription:
    r"""Subscription
    Standard Subscription serializer.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: SubscriptionCreatedBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    frequency: SubscriptionFrequencyEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('frequency') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    next_delivery_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_delivery_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    summary: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('summary') }})
    target_type: SubscriptionTargetTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_type') }})
    target_value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('target_value') }})
    bysetpos: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('bysetpos'), 'exclude': lambda f: f is None }})
    byweekday: Optional[list[SubscriptionByweekdayEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('byweekday'), 'exclude': lambda f: f is None }})
    count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('count'), 'exclude': lambda f: f is None }})
    dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard'), 'exclude': lambda f: f is None }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }})
    insight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('insight'), 'exclude': lambda f: f is None }})
    interval: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('interval'), 'exclude': lambda f: f is None }})
    invite_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('invite_message'), 'exclude': lambda f: f is None }})
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('title'), 'exclude': lambda f: f is None }})
    until_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('until_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    