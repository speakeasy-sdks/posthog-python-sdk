from __future__ import annotations
import dataclasses
from ..shared import filteraction as shared_filteraction
from ..shared import filterevent as shared_filterevent
from ..shared import property as shared_property
from dataclasses_json import Undefined, dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GenericInsights:
    actions: Optional[list[shared_filteraction.FilterAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('actions'), 'exclude': lambda f: f is None }})
    date_from: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_from'), 'exclude': lambda f: f is None }})
    date_to: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('date_to'), 'exclude': lambda f: f is None }})
    events: Optional[list[shared_filterevent.FilterEvent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('events'), 'exclude': lambda f: f is None }})
    filter_test_accounts: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter_test_accounts'), 'exclude': lambda f: f is None }})
    properties: Optional[shared_property.Property] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties'), 'exclude': lambda f: f is None }})
    