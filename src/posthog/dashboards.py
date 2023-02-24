import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Dashboards:
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

    
    def dashboards_create(self, request: operations.DashboardsCreateRequest) -> operations.DashboardsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DashboardOutput])
                res.dashboard = out

        return res

    
    def dashboards_destroy(self, request: operations.DashboardsDestroyRequest) -> operations.DashboardsDestroyResponse:
        r"""Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 405:
            pass

        return res

    
    def dashboards_list(self, request: operations.DashboardsListRequest) -> operations.DashboardsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedDashboardList])
                res.paginated_dashboard_list = out

        return res

    
    def dashboards_move_tile_partial_update(self, request: operations.DashboardsMoveTilePartialUpdateRequest) -> operations.DashboardsMoveTilePartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/{id}/move_tile/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsMoveTilePartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DashboardOutput])
                res.dashboard = out

        return res

    
    def dashboards_partial_update(self, request: operations.DashboardsPartialUpdateRequest) -> operations.DashboardsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DashboardOutput])
                res.dashboard = out

        return res

    
    def dashboards_retrieve(self, request: operations.DashboardsRetrieveRequest) -> operations.DashboardsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DashboardOutput])
                res.dashboard = out

        return res

    
    def dashboards_update(self, request: operations.DashboardsUpdateRequest) -> operations.DashboardsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/dashboards/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DashboardsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.DashboardOutput])
                res.dashboard = out

        return res

    