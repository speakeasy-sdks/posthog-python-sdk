import dataclasses



@dataclasses.dataclass
class SubscriptionsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SubscriptionsDestroyRequest:
    path_params: SubscriptionsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class SubscriptionsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    