import dataclasses



@dataclasses.dataclass
class CohortsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class CohortsDestroyRequest:
    path_params: CohortsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class CohortsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    