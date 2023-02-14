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
class IntegrationCreatedBy:
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('email') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    distinct_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id') }})
    first_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('first_name') }})
    
class IntegrationKindEnum(str, Enum):
    SLACK = "slack"


@dataclass_json
@dataclasses.dataclass
class Integration:
    r"""Integration
    Standard Integration serializer.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    created_by: IntegrationCreatedBy = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_by') }})
    errors: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('errors') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    kind: IntegrationKindEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('kind') }})
    config: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config') }})
    

@dataclass_json
@dataclasses.dataclass
class IntegrationInput:
    r"""IntegrationInput
    Standard Integration serializer.
    """
    
    kind: IntegrationKindEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('kind') }, 'form': { 'field_name': 'kind' }, 'multipart_form': { 'field_name': 'kind' }})
    config: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('config') }, 'form': { 'field_name': 'config', 'json': True }, 'multipart_form': { 'field_name': 'config', 'json': True }})
    