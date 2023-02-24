from __future__ import annotations
import dataclasses
from ..shared import annotation as shared_annotation
from typing import Optional


@dataclasses.dataclass
class AnnotationsUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AnnotationsUpdateRequests:
    annotation: Optional[shared_annotation.AnnotationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    annotation1: Optional[shared_annotation.AnnotationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    annotation2: Optional[shared_annotation.AnnotationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class AnnotationsUpdateRequest:
    path_params: AnnotationsUpdatePathParams = dataclasses.field()
    request: Optional[AnnotationsUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class AnnotationsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    annotation: Optional[shared_annotation.Annotation] = dataclasses.field(default=None)
    