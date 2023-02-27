from __future__ import annotations
import dataclasses
from ..shared import paginatedfeatureflagroleaccesslist as shared_paginatedfeatureflagroleaccesslist
from typing import Optional


@dataclasses.dataclass
class FeatureFlagsRoleAccessListPathParams:
    parent_lookup_feature_flag_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_feature_flag_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessListRequest:
    path_params: FeatureFlagsRoleAccessListPathParams = dataclasses.field()
    query_params: FeatureFlagsRoleAccessListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class FeatureFlagsRoleAccessListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_feature_flag_role_access_list: Optional[shared_paginatedfeatureflagroleaccesslist.PaginatedFeatureFlagRoleAccessList] = dataclasses.field(default=None)
    