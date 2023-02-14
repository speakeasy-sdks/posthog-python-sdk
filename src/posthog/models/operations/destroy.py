import dataclasses



@dataclasses.dataclass
class DestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DestroyRequest:
    path_params: DestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    