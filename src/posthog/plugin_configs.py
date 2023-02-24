import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class PluginConfigs:
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

    
    def plugin_configs_create(self, request: operations.PluginConfigsCreateRequest) -> operations.PluginConfigsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    
    def plugin_configs_destroy(self, request: operations.PluginConfigsDestroyRequest) -> operations.PluginConfigsDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def plugin_configs_frontend_retrieve(self, request: operations.PluginConfigsFrontendRetrieveRequest) -> operations.PluginConfigsFrontendRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{id}/frontend/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsFrontendRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    
    def plugin_configs_job_create(self, request: operations.PluginConfigsJobCreateRequest) -> operations.PluginConfigsJobCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{id}/job/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsJobCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    
    def plugin_configs_list(self, request: operations.PluginConfigsListRequest) -> operations.PluginConfigsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedPluginConfigList])
                res.paginated_plugin_config_list = out

        return res

    
    def plugin_configs_logs_list(self, request: operations.PluginConfigsLogsListRequest) -> operations.PluginConfigsLogsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{parent_lookup_plugin_config_id}/logs/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsLogsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedPluginLogEntryList])
                res.paginated_plugin_log_entry_list = out

        return res

    
    def plugin_configs_partial_update(self, request: operations.PluginConfigsPartialUpdateRequest) -> operations.PluginConfigsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    
    def plugin_configs_rearrange_partial_update(self, request: operations.PluginConfigsRearrangePartialUpdateRequest) -> operations.PluginConfigsRearrangePartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/rearrange/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsRearrangePartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    
    def plugin_configs_retrieve(self, request: operations.PluginConfigsRetrieveRequest) -> operations.PluginConfigsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    
    def plugin_configs_update(self, request: operations.PluginConfigsUpdateRequest) -> operations.PluginConfigsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/plugin_configs/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginConfigsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PluginConfig])
                res.plugin_config = out

        return res

    