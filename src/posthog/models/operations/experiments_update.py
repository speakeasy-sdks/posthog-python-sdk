import dataclasses
from ..shared import experiment as shared_experiment
from typing import Optional


@dataclasses.dataclass
class ExperimentsUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExperimentsUpdateRequests:
    experiment: Optional[shared_experiment.ExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    experiment1: Optional[shared_experiment.ExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    experiment2: Optional[shared_experiment.ExperimentInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class ExperimentsUpdateRequest:
    path_params: ExperimentsUpdatePathParams = dataclasses.field()
    request: ExperimentsUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class ExperimentsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    experiment: Optional[shared_experiment.Experiment] = dataclasses.field(default=None)
    