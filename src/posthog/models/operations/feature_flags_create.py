import dataclasses
from ..shared import featureflag as shared_featureflag
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsCreateRequests:
    feature_flag: Optional[shared_featureflag.FeatureFlagInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    feature_flag1: Optional[shared_featureflag.FeatureFlagInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    feature_flag2: Optional[shared_featureflag.FeatureFlagInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class FeatureFlagsCreateRequest:
    path_params: FeatureFlagsCreatePathParams = dataclasses.field()
    request: FeatureFlagsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag: Optional[shared_featureflag.FeatureFlag] = dataclasses.field(default=None)
    