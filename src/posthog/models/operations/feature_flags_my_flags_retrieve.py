from __future__ import annotations
import dataclasses
from ..shared import featureflag as shared_featureflag
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsMyFlagsRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsMyFlagsRetrieveRequest:
    path_params: FeatureFlagsMyFlagsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsMyFlagsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag: Optional[shared_featureflag.FeatureFlag] = dataclasses.field(default=None)
    