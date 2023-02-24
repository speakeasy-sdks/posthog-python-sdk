from __future__ import annotations
import dataclasses
from ..shared import paginatedexperimentlist as shared_paginatedexperimentlist
from typing import Optional


@dataclasses.dataclass
class ExperimentsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExperimentsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ExperimentsListRequest:
    path_params: ExperimentsListPathParams = dataclasses.field()
    query_params: ExperimentsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ExperimentsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_experiment_list: Optional[shared_paginatedexperimentlist.PaginatedExperimentList] = dataclasses.field(default=None)
    