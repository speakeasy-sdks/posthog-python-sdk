import dataclasses



@dataclasses.dataclass
class DashboardTemplatesRepositoryRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DashboardTemplatesRepositoryRetrieveRequest:
    path_params: DashboardTemplatesRepositoryRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class DashboardTemplatesRepositoryRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    