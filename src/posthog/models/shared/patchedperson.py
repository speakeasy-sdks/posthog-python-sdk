import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Any, Optional


@dataclass_json
@dataclasses.dataclass
class PatchedPersonInput:
    properties: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties') }, 'form': { 'field_name': 'properties', 'json': True }, 'multipart_form': { 'field_name': 'properties', 'json': True }})
    