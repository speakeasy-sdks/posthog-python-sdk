import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Roles:
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

    
    def roles_create(self, request: operations.RolesCreateRequest) -> operations.RolesCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Role])
                res.role = out

        return res

    
    def roles_destroy(self, request: operations.RolesDestroyRequest) -> operations.RolesDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def roles_list(self, request: operations.RolesListRequest) -> operations.RolesListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedRoleList])
                res.paginated_role_list = out

        return res

    
    def roles_partial_update(self, request: operations.RolesPartialUpdateRequest) -> operations.RolesPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Role])
                res.role = out

        return res

    
    def roles_retrieve(self, request: operations.RolesRetrieveRequest) -> operations.RolesRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Role])
                res.role = out

        return res

    
    def roles_role_memberships_create(self, request: operations.RolesRoleMembershipsCreateRequest) -> operations.RolesRoleMembershipsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{parent_lookup_role_id}/role_memberships/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesRoleMembershipsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.RoleMembershipOutput])
                res.role_membership = out

        return res

    
    def roles_role_memberships_destroy(self, request: operations.RolesRoleMembershipsDestroyRequest) -> operations.RolesRoleMembershipsDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{parent_lookup_role_id}/role_memberships/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesRoleMembershipsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def roles_role_memberships_list(self, request: operations.RolesRoleMembershipsListRequest) -> operations.RolesRoleMembershipsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{parent_lookup_role_id}/role_memberships/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesRoleMembershipsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedRoleMembershipList])
                res.paginated_role_membership_list = out

        return res

    
    def roles_update(self, request: operations.RolesUpdateRequest) -> operations.RolesUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/roles/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.RolesUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Role])
                res.role = out

        return res

    