from __future__ import annotations
import dataclasses
from ..shared import dashboard as shared_dashboard
from typing import Optional


@dataclasses.dataclass
class DashboardsUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DashboardsUpdateRequests:
    dashboard: Optional[shared_dashboard.DashboardInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    dashboard1: Optional[shared_dashboard.DashboardInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    dashboard2: Optional[shared_dashboard.DashboardInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class DashboardsUpdateRequest:
    path_params: DashboardsUpdatePathParams = dataclasses.field()
    request: Optional[DashboardsUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class DashboardsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dashboard: Optional[shared_dashboard.DashboardOutput] = dataclasses.field(default=None)
    