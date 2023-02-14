import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils
from typing import Optional

class PatchedAnnotationCreationTypeEnum(str, Enum):
    USR = "USR"
    GIT = "GIT"

class PatchedAnnotationScopeEnum(str, Enum):
    DASHBOARD_ITEM = "dashboard_item"
    PROJECT = "project"
    ORGANIZATION = "organization"


@dataclass_json
@dataclasses.dataclass
class PatchedAnnotationInput:
    content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('content') }, 'form': { 'field_name': 'content' }, 'multipart_form': { 'field_name': 'content' }})
    creation_type: Optional[PatchedAnnotationCreationTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('creation_type') }, 'form': { 'field_name': 'creation_type' }, 'multipart_form': { 'field_name': 'creation_type' }})
    dashboard_item: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard_item') }, 'form': { 'field_name': 'dashboard_item' }, 'multipart_form': { 'field_name': 'dashboard_item' }})
    date_marker: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_marker'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }, 'form': { 'field_name': 'date_marker' }, 'multipart_form': { 'field_name': 'date_marker' }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    scope: Optional[PatchedAnnotationScopeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('scope') }, 'form': { 'field_name': 'scope' }, 'multipart_form': { 'field_name': 'scope' }})
    