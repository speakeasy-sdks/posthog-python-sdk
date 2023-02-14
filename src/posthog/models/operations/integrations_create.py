import dataclasses
from ..shared import integration as shared_integration
from typing import Optional


@dataclasses.dataclass
class IntegrationsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class IntegrationsCreateRequests:
    integration: Optional[shared_integration.IntegrationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    integration1: Optional[shared_integration.IntegrationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    integration2: Optional[shared_integration.IntegrationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class IntegrationsCreateRequest:
    path_params: IntegrationsCreatePathParams = dataclasses.field()
    request: IntegrationsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class IntegrationsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    integration: Optional[shared_integration.Integration] = dataclasses.field(default=None)
    