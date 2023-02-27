from __future__ import annotations
import dataclasses
from ..shared import dashboard as shared_dashboard
from ..shared import patcheddashboard as shared_patcheddashboard
from typing import Optional


@dataclasses.dataclass
class DashboardsMoveTilePartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DashboardsMoveTilePartialUpdateRequests:
    patched_dashboard: Optional[shared_patcheddashboard.PatchedDashboardInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_dashboard1: Optional[shared_patcheddashboard.PatchedDashboardInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_dashboard2: Optional[shared_patcheddashboard.PatchedDashboardInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class DashboardsMoveTilePartialUpdateRequest:
    path_params: DashboardsMoveTilePartialUpdatePathParams = dataclasses.field()
    request: Optional[DashboardsMoveTilePartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class DashboardsMoveTilePartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    dashboard: Optional[shared_dashboard.DashboardOutput] = dataclasses.field(default=None)
    