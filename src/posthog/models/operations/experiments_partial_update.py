from __future__ import annotations
import dataclasses
from ..shared import experiment as shared_experiment
from ..shared import patchedexperiment as shared_patchedexperiment
from typing import Optional


@dataclasses.dataclass
class ExperimentsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExperimentsPartialUpdateRequests:
    patched_experiment: Optional[shared_patchedexperiment.PatchedExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_experiment1: Optional[shared_patchedexperiment.PatchedExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_experiment2: Optional[shared_patchedexperiment.PatchedExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ExperimentsPartialUpdateRequest:
    path_params: ExperimentsPartialUpdatePathParams = dataclasses.field()
    request: Optional[ExperimentsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class ExperimentsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    experiment: Optional[shared_experiment.Experiment] = dataclasses.field(default=None)
    