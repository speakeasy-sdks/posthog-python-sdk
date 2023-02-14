import dataclasses
import dateutil.parser
from dataclasses_json import dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class DashboardInput:
    r"""DashboardInput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    delete_insights: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('delete_insights') }, 'form': { 'field_name': 'delete_insights' }, 'multipart_form': { 'field_name': 'delete_insights' }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }, 'form': { 'field_name': 'deleted' }, 'multipart_form': { 'field_name': 'deleted' }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }, 'form': { 'field_name': 'description' }, 'multipart_form': { 'field_name': 'description' }})
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }, 'form': { 'field_name': 'filters', 'json': True }, 'multipart_form': { 'field_name': 'filters', 'json': True }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }, 'form': { 'field_name': 'name' }, 'multipart_form': { 'field_name': 'name' }})
    pinned: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pinned') }, 'form': { 'field_name': 'pinned' }, 'multipart_form': { 'field_name': 'pinned' }})
    restriction_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('restriction_level') }, 'form': { 'field_name': 'restriction_level' }, 'multipart_form': { 'field_name': 'restriction_level' }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }, 'form': { 'field_name': 'tags', 'json': True }, 'multipart_form': { 'field_name': 'tags', 'json': True }})
    use_dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_dashboard') }, 'form': { 'field_name': 'use_dashboard' }, 'multipart_form': { 'field_name': 'use_dashboard' }})
    use_template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('use_template') }, 'form': { 'field_name': 'use_template' }, 'multipart_form': { 'field_name': 'use_template' }})
    

@dataclass_json
@dataclasses.dataclass
class DashboardCreatedBy:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    distinct_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id') }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name') }})
    
class DashboardCreationModeEnum(str, Enum):
    DEFAULT = "default"
    TEMPLATE = "template"
    DUPLICATE = "duplicate"


@dataclass_json
@dataclasses.dataclass
class DashboardOutput:
    r"""DashboardOutput
    Serializer mixin that resolves appropriate response for tags depending on license.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: DashboardCreatedBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    creation_mode: DashboardCreationModeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('creation_mode') }})
    effective_privilege_level: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('effective_privilege_level') }})
    effective_restriction_level: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('effective_restriction_level') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_shared: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_shared') }})
    tiles: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tiles') }})
    deleted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('deleted') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    filters: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filters') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    pinned: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pinned') }})
    restriction_level: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('restriction_level') }})
    tags: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tags') }})
    