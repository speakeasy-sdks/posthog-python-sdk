import dataclasses
from ..shared import paginatedfeatureflaglist as shared_paginatedfeatureflaglist
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class FeatureFlagsListRequest:
    path_params: FeatureFlagsListPathParams = dataclasses.field()
    query_params: FeatureFlagsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_feature_flag_list: Optional[shared_paginatedfeatureflaglist.PaginatedFeatureFlagList] = dataclasses.field(default=None)
    