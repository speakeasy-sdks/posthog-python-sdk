import dataclasses
from ..shared import dashboard as shared_dashboard
from typing import Optional


@dataclasses.dataclass
class DashboardsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DashboardsRetrieveRequest:
    path_params: DashboardsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class DashboardsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dashboard: Optional[shared_dashboard.DashboardOutput] = dataclasses.field(default=None)
    