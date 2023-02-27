from __future__ import annotations
import dataclasses
from ..shared import paginatedintegrationlist as shared_paginatedintegrationlist
from typing import Optional


@dataclasses.dataclass
class IntegrationsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class IntegrationsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class IntegrationsListRequest:
    path_params: IntegrationsListPathParams = dataclasses.field()
    query_params: IntegrationsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class IntegrationsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_integration_list: Optional[shared_paginatedintegrationlist.PaginatedIntegrationList] = dataclasses.field(default=None)
    