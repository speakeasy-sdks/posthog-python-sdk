import dataclasses



@dataclasses.dataclass
class HooksDestroyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class HooksDestroyRequest:
    path_params: HooksDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class HooksDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    