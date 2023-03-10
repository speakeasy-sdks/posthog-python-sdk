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
class CohortInput:
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'filters', 'json': True }, 'multipart_form': { 'field_name': 'filters', 'json': True }})
    groups: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groups'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'groups', 'json': True }, 'multipart_form': { 'field_name': 'groups', 'json': True }})
    is_static: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_static'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'is_static' }, 'multipart_form': { 'field_name': 'is_static' }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CohortCreatedBy:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    distinct_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id'), 'exclude': lambda f: f is None }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Cohort:
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('count') }})
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: CohortCreatedBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    errors_calculating: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors_calculating') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_calculating: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_calculating') }})
    last_calculation: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('last_calculation'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description'), 'exclude': lambda f: f is None }})
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters'), 'exclude': lambda f: f is None }})
    groups: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('groups'), 'exclude': lambda f: f is None }})
    is_static: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_static'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name'), 'exclude': lambda f: f is None }})
    