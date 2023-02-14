import dataclasses



@dataclasses.dataclass
class FeatureFlagsRoleAccessDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_feature_flag_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_feature_flag_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessDestroyRequest:
    path_params: FeatureFlagsRoleAccessDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    