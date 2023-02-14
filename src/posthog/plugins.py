import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Plugins:
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

    
    def plugins_activity_retrieve(self, request: operations.PluginsActivityRetrieveRequest) -> operations.PluginsActivityRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/activity/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsActivityRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_check_for_updates_retrieve(self, request: operations.PluginsCheckForUpdatesRetrieveRequest) -> operations.PluginsCheckForUpdatesRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/check_for_updates/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsCheckForUpdatesRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_create(self, request: operations.PluginsCreateRequest) -> operations.PluginsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_destroy(self, request: operations.PluginsDestroyRequest) -> operations.PluginsDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def plugins_list(self, request: operations.PluginsListRequest) -> operations.PluginsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedPluginList])
                res.paginated_plugin_list = out

        return res

    
    def plugins_partial_update(self, request: operations.PluginsPartialUpdateRequest) -> operations.PluginsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_repository_retrieve(self, request: operations.PluginsRepositoryRetrieveRequest) -> operations.PluginsRepositoryRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/repository/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsRepositoryRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_retrieve(self, request: operations.PluginsRetrieveRequest) -> operations.PluginsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_source_retrieve(self, request: operations.PluginsSourceRetrieveRequest) -> operations.PluginsSourceRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/source/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsSourceRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_update(self, request: operations.PluginsUpdateRequest) -> operations.PluginsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_update_source_partial_update(self, request: operations.PluginsUpdateSourcePartialUpdateRequest) -> operations.PluginsUpdateSourcePartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/update_source/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsUpdateSourcePartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    
    def plugins_upgrade_create(self, request: operations.PluginsUpgradeCreateRequest) -> operations.PluginsUpgradeCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/plugins/{id}/upgrade/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PluginsUpgradeCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Plugin])
                res.plugin = out

        return res

    