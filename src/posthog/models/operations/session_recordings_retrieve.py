import dataclasses



@dataclasses.dataclass
class SessionRecordingsRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingsRetrieveRequest:
    path_params: SessionRecordingsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    