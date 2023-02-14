import dataclasses



@dataclasses.dataclass
class IngestionWarningsRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class IngestionWarningsRetrieveRequest:
    path_params: IngestionWarningsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class IngestionWarningsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    