import dataclasses



@dataclasses.dataclass
class SessionRecordingsPropertiesRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingsPropertiesRetrieveRequest:
    path_params: SessionRecordingsPropertiesRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingsPropertiesRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    