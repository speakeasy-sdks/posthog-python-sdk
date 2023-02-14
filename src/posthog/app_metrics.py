import requests
from . import utils
from posthog.models import operations

class AppMetrics:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def app_metrics_error_details_retrieve(self, request: operations.AppMetricsErrorDetailsRetrieveRequest) -> operations.AppMetricsErrorDetailsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/app_metrics/{id}/error_details/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.AppMetricsErrorDetailsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def app_metrics_historical_exports_retrieve(self, request: operations.AppMetricsHistoricalExportsRetrieveRequest) -> operations.AppMetricsHistoricalExportsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/app_metrics/{parent_lookup_plugin_config_id}/historical_exports/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.AppMetricsHistoricalExportsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def app_metrics_historical_exports_retrieve_2(self, request: operations.AppMetricsHistoricalExportsRetrieve2Request) -> operations.AppMetricsHistoricalExportsRetrieve2Response:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/app_metrics/{parent_lookup_plugin_config_id}/historical_exports/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.AppMetricsHistoricalExportsRetrieve2Response(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def app_metrics_retrieve(self, request: operations.AppMetricsRetrieveRequest) -> operations.AppMetricsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/app_metrics/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.AppMetricsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    