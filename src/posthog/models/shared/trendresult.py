from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import genericinsights as shared_genericinsights
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from marshmallow import fields
from posthog import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrendResult:
    data: list[int] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('data') }})
    days: list[date] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('days') }})
    filter: shared_genericinsights.GenericInsights = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filter') }})
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    labels: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('labels') }})
    