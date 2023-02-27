from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import userbasic as shared_userbasic
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityLog:
    activity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('activity') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    scope: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('scope') }})
    unread: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('unread') }})
    user: shared_userbasic.UserBasic = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('user') }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    detail: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detail'), 'exclude': lambda f: f is None }})
    is_system: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_system'), 'exclude': lambda f: f is None }})
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item_id'), 'exclude': lambda f: f is None }})
    organization_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('organization_id'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ActivityLogInput:
    activity: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('activity') }, 'form': { 'field_name': 'activity' }, 'multipart_form': { 'field_name': 'activity' }})
    scope: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('scope') }, 'form': { 'field_name': 'scope' }, 'multipart_form': { 'field_name': 'scope' }})
    user: shared_userbasic.UserBasicInput = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('user') }, 'form': { 'field_name': 'user', 'json': True }, 'multipart_form': { 'field_name': 'user', 'json': True }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'created_at' }, 'multipart_form': { 'field_name': 'created_at' }})
    detail: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('detail'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'detail', 'json': True }, 'multipart_form': { 'field_name': 'detail', 'json': True }})
    is_system: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_system'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'is_system' }, 'multipart_form': { 'field_name': 'is_system' }})
    item_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('item_id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'item_id' }, 'multipart_form': { 'field_name': 'item_id' }})
    organization_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('organization_id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'organization_id' }, 'multipart_form': { 'field_name': 'organization_id' }})
    