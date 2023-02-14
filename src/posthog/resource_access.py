import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class ResourceAccess:
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

    
    def resource_access_create(self, request: operations.ResourceAccessCreateRequest) -> operations.ResourceAccessCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/resource_access/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ResourceAccessCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationResourceAccess])
                res.organization_resource_access = out

        return res

    
    def resource_access_destroy(self, request: operations.ResourceAccessDestroyRequest) -> operations.ResourceAccessDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/resource_access/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ResourceAccessDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def resource_access_list(self, request: operations.ResourceAccessListRequest) -> operations.ResourceAccessListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/resource_access/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ResourceAccessListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedOrganizationResourceAccessList])
                res.paginated_organization_resource_access_list = out

        return res

    
    def resource_access_partial_update(self, request: operations.ResourceAccessPartialUpdateRequest) -> operations.ResourceAccessPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/resource_access/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ResourceAccessPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationResourceAccess])
                res.organization_resource_access = out

        return res

    
    def resource_access_retrieve(self, request: operations.ResourceAccessRetrieveRequest) -> operations.ResourceAccessRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/resource_access/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ResourceAccessRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationResourceAccess])
                res.organization_resource_access = out

        return res

    
    def resource_access_update(self, request: operations.ResourceAccessUpdateRequest) -> operations.ResourceAccessUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/resource_access/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ResourceAccessUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationResourceAccess])
                res.organization_resource_access = out

        return res

    