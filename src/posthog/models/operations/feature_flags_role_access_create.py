import dataclasses
from ..shared import featureflagroleaccess as shared_featureflagroleaccess
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsRoleAccessCreatePathParams:
    parent_lookup_feature_flag_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_feature_flag_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessCreateRequests:
    feature_flag_role_access: Optional[shared_featureflagroleaccess.FeatureFlagRoleAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    feature_flag_role_access1: Optional[shared_featureflagroleaccess.FeatureFlagRoleAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    feature_flag_role_access2: Optional[shared_featureflagroleaccess.FeatureFlagRoleAccessInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessCreateRequest:
    path_params: FeatureFlagsRoleAccessCreatePathParams = dataclasses.field()
    request: FeatureFlagsRoleAccessCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag_role_access: Optional[shared_featureflagroleaccess.FeatureFlagRoleAccessOutput] = dataclasses.field(default=None)
    