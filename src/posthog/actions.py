import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Actions:
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

    
    def actions_count_retrieve(self, request: operations.ActionsCountRetrieveRequest) -> operations.ActionsCountRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/{id}/count/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsCountRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Action])
                res.action = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    
    def actions_create(self, request: operations.ActionsCreateRequest) -> operations.ActionsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("POST", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Action])
                res.action = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    
    def actions_destroy(self, request: operations.ActionsDestroyRequest) -> operations.ActionsDestroyResponse:
        r"""Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/{id}/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("DELETE", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 405:
            pass

        return res

    
    def actions_list(self, request: operations.ActionsListRequest) -> operations.ActionsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedActionList])
                res.paginated_action_list = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    
    def actions_partial_update(self, request: operations.ActionsPartialUpdateRequest) -> operations.ActionsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("PATCH", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Action])
                res.action = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    
    def actions_people_retrieve(self, request: operations.ActionsPeopleRetrieveRequest) -> operations.ActionsPeopleRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/people/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsPeopleRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Action])
                res.action = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    
    def actions_retrieve(self, request: operations.ActionsRetrieveRequest) -> operations.ActionsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/{id}/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Action])
                res.action = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    
    def actions_update(self, request: operations.ActionsUpdateRequest) -> operations.ActionsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/actions/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("PUT", url, params=query_params, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ActionsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Action])
                res.action = out
            if utils.match_content_type(content_type, "text/csv"):
                res.body = r.content

        return res

    