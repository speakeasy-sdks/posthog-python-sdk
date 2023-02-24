from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class SessionRecordingsRetrieve2PathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingsRetrieve2Request:
    path_params: SessionRecordingsRetrieve2PathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingsRetrieve2Response:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    