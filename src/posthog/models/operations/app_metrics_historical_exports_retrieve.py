import dataclasses



@dataclasses.dataclass
class AppMetricsHistoricalExportsRetrievePathParams:
    parent_lookup_plugin_config_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_plugin_config_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AppMetricsHistoricalExportsRetrieveRequest:
    path_params: AppMetricsHistoricalExportsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class AppMetricsHistoricalExportsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    