import dataclasses
from ..shared import activitylog as shared_activitylog
from typing import Optional


@dataclasses.dataclass
class ActivityLogImportantChangesRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ActivityLogImportantChangesRetrieveRequest:
    path_params: ActivityLogImportantChangesRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class ActivityLogImportantChangesRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    activity_log: Optional[shared_activitylog.ActivityLog] = dataclasses.field(default=None)
    