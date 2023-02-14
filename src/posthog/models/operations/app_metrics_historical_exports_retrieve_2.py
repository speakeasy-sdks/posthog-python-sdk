import dataclasses



@dataclasses.dataclass
class AppMetricsHistoricalExportsRetrieve2PathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_plugin_config_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_plugin_config_id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class AppMetricsHistoricalExportsRetrieve2Request:
    path_params: AppMetricsHistoricalExportsRetrieve2PathParams = dataclasses.field()
    

@dataclasses.dataclass
class AppMetricsHistoricalExportsRetrieve2Response:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    