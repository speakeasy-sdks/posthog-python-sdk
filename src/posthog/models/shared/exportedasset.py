from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from posthog import utils
from typing import Any, Optional

class ExportedAssetExportFormatEnum(str, Enum):
    IMAGE_PNG = "image/png"
    APPLICATION_PDF = "application/pdf"
    TEXT_CSV = "text/csv"


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExportedAsset:
    r"""ExportedAsset
    Standard ExportedAsset serializer that doesn't return content.
    """
    
    created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    export_format: ExportedAssetExportFormatEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('export_format') }})
    filename: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('filename') }})
    has_content: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('has_content') }})
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard'), 'exclude': lambda f: f is None }})
    export_context: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('export_context'), 'exclude': lambda f: f is None }})
    insight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('insight'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ExportedAssetInput:
    r"""ExportedAssetInput
    Standard ExportedAsset serializer that doesn't return content.
    """
    
    export_format: ExportedAssetExportFormatEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('export_format') }, 'form': { 'field_name': 'export_format' }, 'multipart_form': { 'field_name': 'export_format' }})
    dashboard: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dashboard'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'dashboard' }, 'multipart_form': { 'field_name': 'dashboard' }})
    export_context: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('export_context'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'export_context', 'json': True }, 'multipart_form': { 'field_name': 'export_context', 'json': True }})
    insight: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('insight'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'insight' }, 'multipart_form': { 'field_name': 'insight' }})
    