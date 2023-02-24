from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils
from typing import Optional

class OrganizationResourceAccessResourceEnum(str, Enum):
    FEATURE_FLAGS = "feature flags"
    EXPERIMENTS = "experiments"
    COHORTS = "cohorts"
    DATA_MANAGEMENT = "data management"
    SESSION_RECORDINGS = "session recordings"
    INSIGHTS = "insights"
    DASHBOARDS = "dashboards"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationResourceAccessInput:
    resource: OrganizationResourceAccessResourceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource') }, 'form': { 'field_name': 'resource' }, 'multipart_form': { 'field_name': 'resource' }})
    access_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('access_level'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'access_level' }, 'multipart_form': { 'field_name': 'access_level' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationResourceAccess:
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('organization') }})
    resource: OrganizationResourceAccessResourceEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('resource') }})
    updated_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('updated_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    access_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('access_level'), 'exclude': lambda f: f is None }})
    