from __future__ import annotations
import dataclasses
from ..shared import dashboardtemplate as shared_dashboardtemplate
from typing import Optional


@dataclasses.dataclass
class DashboardTemplatesCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DashboardTemplatesCreateRequests:
    dashboard_template: Optional[shared_dashboardtemplate.DashboardTemplate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    dashboard_template1: Optional[shared_dashboardtemplate.DashboardTemplate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    dashboard_template2: Optional[shared_dashboardtemplate.DashboardTemplate] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class DashboardTemplatesCreateRequest:
    path_params: DashboardTemplatesCreatePathParams = dataclasses.field()
    request: DashboardTemplatesCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class DashboardTemplatesCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    