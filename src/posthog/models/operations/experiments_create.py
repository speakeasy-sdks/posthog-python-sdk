from __future__ import annotations
import dataclasses
from ..shared import experiment as shared_experiment
from typing import Optional


@dataclasses.dataclass
class ExperimentsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExperimentsCreateRequests:
    experiment: Optional[shared_experiment.ExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    experiment1: Optional[shared_experiment.ExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    experiment2: Optional[shared_experiment.ExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ExperimentsCreateRequest:
    path_params: ExperimentsCreatePathParams = dataclasses.field()
    request: ExperimentsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class ExperimentsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    experiment: Optional[shared_experiment.Experiment] = dataclasses.field(default=None)
    