import dataclasses
from ..shared import annotation as shared_annotation
from typing import Optional


@dataclasses.dataclass
class AnnotationsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AnnotationsRetrieveRequest:
    path_params: AnnotationsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class AnnotationsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    annotation: Optional[shared_annotation.Annotation] = dataclasses.field(default=None)
    