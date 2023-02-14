import dataclasses



@dataclasses.dataclass
class UploadedMediaCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UploadedMediaCreateRequest:
    path_params: UploadedMediaCreatePathParams = dataclasses.field()
    

@dataclasses.dataclass
class UploadedMediaCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    