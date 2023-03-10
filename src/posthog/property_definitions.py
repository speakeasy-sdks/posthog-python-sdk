import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class PropertyDefinitions:
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

    
    def property_definitions_list(self, request: operations.PropertyDefinitionsListRequest) -> operations.PropertyDefinitionsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/property_definitions/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.PropertyDefinitionsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedPropertyDefinitionList])
                res.paginated_property_definition_list = out

        return res

    
    def property_definitions_partial_update(self, request: operations.PropertyDefinitionsPartialUpdateRequest) -> operations.PropertyDefinitionsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/property_definitions/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PropertyDefinitionsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PropertyDefinition])
                res.property_definition = out

        return res

    
    def property_definitions_retrieve(self, request: operations.PropertyDefinitionsRetrieveRequest) -> operations.PropertyDefinitionsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/property_definitions/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PropertyDefinitionsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PropertyDefinition])
                res.property_definition = out

        return res

    
    def property_definitions_update(self, request: operations.PropertyDefinitionsUpdateRequest) -> operations.PropertyDefinitionsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/property_definitions/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PropertyDefinitionsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PropertyDefinition])
                res.property_definition = out

        return res

    