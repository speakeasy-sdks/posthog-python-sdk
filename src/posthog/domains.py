import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Domains:
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

    
    def domains_create(self, request: operations.DomainsCreateRequest) -> operations.DomainsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationDomain])
                res.organization_domain = out

        return res

    
    def domains_destroy(self, request: operations.DomainsDestroyRequest) -> operations.DomainsDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def domains_list(self, request: operations.DomainsListRequest) -> operations.DomainsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedOrganizationDomainList])
                res.paginated_organization_domain_list = out

        return res

    
    def domains_partial_update(self, request: operations.DomainsPartialUpdateRequest) -> operations.DomainsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationDomain])
                res.organization_domain = out

        return res

    
    def domains_retrieve(self, request: operations.DomainsRetrieveRequest) -> operations.DomainsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationDomain])
                res.organization_domain = out

        return res

    
    def domains_update(self, request: operations.DomainsUpdateRequest) -> operations.DomainsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationDomain])
                res.organization_domain = out

        return res

    
    def domains_verify_create(self, request: operations.DomainsVerifyCreateRequest) -> operations.DomainsVerifyCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/domains/{id}/verify/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsVerifyCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationDomain])
                res.organization_domain = out

        return res

    