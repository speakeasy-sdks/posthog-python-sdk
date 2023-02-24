from __future__ import annotations
import dataclasses
from ..shared import experiment as shared_experiment
from typing import Optional


@dataclasses.dataclass
class ExperimentsSecondaryResultsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ExperimentsSecondaryResultsRetrieveRequest:
    path_params: ExperimentsSecondaryResultsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class ExperimentsSecondaryResultsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    experiment: Optional[shared_experiment.Experiment] = dataclasses.field(default=None)
    