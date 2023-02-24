from __future__ import annotations
import dataclasses
from ..shared import featureflag as shared_featureflag
from ..shared import patchedfeatureflag as shared_patchedfeatureflag
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsPartialUpdateRequests:
    patched_feature_flag: Optional[shared_patchedfeatureflag.PatchedFeatureFlagInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_feature_flag1: Optional[shared_patchedfeatureflag.PatchedFeatureFlagInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_feature_flag2: Optional[shared_patchedfeatureflag.PatchedFeatureFlagInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class FeatureFlagsPartialUpdateRequest:
    path_params: FeatureFlagsPartialUpdatePathParams = dataclasses.field()
    request: Optional[FeatureFlagsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class FeatureFlagsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag: Optional[shared_featureflag.FeatureFlag] = dataclasses.field(default=None)
    