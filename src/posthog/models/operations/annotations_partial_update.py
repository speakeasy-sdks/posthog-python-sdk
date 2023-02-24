from __future__ import annotations
import dataclasses
from ..shared import annotation as shared_annotation
from ..shared import patchedannotation as shared_patchedannotation
from typing import Optional


@dataclasses.dataclass
class AnnotationsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AnnotationsPartialUpdateRequests:
    patched_annotation: Optional[shared_patchedannotation.PatchedAnnotationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_annotation1: Optional[shared_patchedannotation.PatchedAnnotationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_annotation2: Optional[shared_patchedannotation.PatchedAnnotationInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class AnnotationsPartialUpdateRequest:
    path_params: AnnotationsPartialUpdatePathParams = dataclasses.field()
    request: Optional[AnnotationsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class AnnotationsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    annotation: Optional[shared_annotation.Annotation] = dataclasses.field(default=None)
    