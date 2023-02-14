import dataclasses



@dataclasses.dataclass
class FeatureFlagsDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsDestroyRequest:
    path_params: FeatureFlagsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    