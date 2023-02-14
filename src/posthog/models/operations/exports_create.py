import dataclasses
from ..shared import exportedasset as shared_exportedasset
from typing import Optional


@dataclasses.dataclass
class ExportsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExportsCreateRequests:
    exported_asset: Optional[shared_exportedasset.ExportedAssetInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    exported_asset1: Optional[shared_exportedasset.ExportedAssetInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    exported_asset2: Optional[shared_exportedasset.ExportedAssetInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ExportsCreateRequest:
    path_params: ExportsCreatePathParams = dataclasses.field()
    request: ExportsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class ExportsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    exported_asset: Optional[shared_exportedasset.ExportedAsset] = dataclasses.field(default=None)
    