from __future__ import annotations
import dataclasses
from ..shared import activitylog as shared_activitylog
from typing import Optional


@dataclasses.dataclass
class ActivityLogBookmarkActivityNotificationCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ActivityLogBookmarkActivityNotificationCreateRequests:
    activity_log: Optional[shared_activitylog.ActivityLogInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    activity_log1: Optional[shared_activitylog.ActivityLogInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    activity_log2: Optional[shared_activitylog.ActivityLogInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ActivityLogBookmarkActivityNotificationCreateRequest:
    path_params: ActivityLogBookmarkActivityNotificationCreatePathParams = dataclasses.field()
    request: ActivityLogBookmarkActivityNotificationCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class ActivityLogBookmarkActivityNotificationCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_log: Optional[shared_activitylog.ActivityLog] = dataclasses.field(default=None)
    