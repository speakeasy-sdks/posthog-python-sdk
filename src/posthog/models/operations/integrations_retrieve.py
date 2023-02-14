import dataclasses
from ..shared import integration as shared_integration
from typing import Optional


@dataclasses.dataclass
class IntegrationsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class IntegrationsRetrieveRequest:
    path_params: IntegrationsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class IntegrationsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    integration: Optional[shared_integration.Integration] = dataclasses.field(default=None)
    