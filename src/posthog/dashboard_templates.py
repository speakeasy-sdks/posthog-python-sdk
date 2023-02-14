import requests
from . import utils
from posthog.models import operations

class DashboardTemplates:
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

    
    def dashboard_templates_create(self, request: operations.DashboardTemplatesCreateRequest) -> operations.DashboardTemplatesCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboard_templates/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardTemplatesCreateResponse(status_code=r.status_code, content_type=content_type)

        return res

    
    def dashboard_templates_repository_retrieve(self, request: operations.DashboardTemplatesRepositoryRetrieveRequest) -> operations.DashboardTemplatesRepositoryRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboard_templates/repository/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardTemplatesRepositoryRetrieveResponse(status_code=r.status_code, content_type=content_type)

        return res

    