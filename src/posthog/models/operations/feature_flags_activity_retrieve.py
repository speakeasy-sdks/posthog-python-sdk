from __future__ import annotations
import dataclasses
from ..shared import featureflag as shared_featureflag
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsActivityRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsActivityRetrieveRequest:
    path_params: FeatureFlagsActivityRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsActivityRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag: Optional[shared_featureflag.FeatureFlag] = dataclasses.field(default=None)
    