from __future__ import annotations
import dataclasses
from ..shared import featureflag as shared_featureflag
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsRetrieveRequest:
    path_params: FeatureFlagsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    feature_flag: Optional[shared_featureflag.FeatureFlag] = dataclasses.field(default=None)
    