import dataclasses
from ..shared import featureflagroleaccess as shared_featureflagroleaccess
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsRoleAccessRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_feature_flag_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_feature_flag_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessRetrieveRequest:
    path_params: FeatureFlagsRoleAccessRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag_role_access: Optional[shared_featureflagroleaccess.FeatureFlagRoleAccessOutput] = dataclasses.field(default=None)
    