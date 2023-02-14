import dataclasses



@dataclasses.dataclass
class SessionRecordingsSnapshotsRetrievePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingsSnapshotsRetrieveRequest:
    path_params: SessionRecordingsSnapshotsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingsSnapshotsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    