import dataclasses
from ..shared import exportedasset as shared_exportedasset
from typing import Optional


@dataclasses.dataclass
class ExportsContentRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExportsContentRetrieveRequest:
    path_params: ExportsContentRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class ExportsContentRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    exported_asset: Optional[shared_exportedasset.ExportedAsset] = dataclasses.field(default=None)
    