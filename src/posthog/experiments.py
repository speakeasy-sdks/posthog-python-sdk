import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Experiments:
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

    
    def experiments_create(self, request: operations.ExperimentsCreateRequest) -> operations.ExperimentsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    
    def experiments_destroy(self, request: operations.ExperimentsDestroyRequest) -> operations.ExperimentsDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def experiments_list(self, request: operations.ExperimentsListRequest) -> operations.ExperimentsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedExperimentList])
                res.paginated_experiment_list = out

        return res

    
    def experiments_partial_update(self, request: operations.ExperimentsPartialUpdateRequest) -> operations.ExperimentsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    
    def experiments_requires_flag_implementation_retrieve(self, request: operations.ExperimentsRequiresFlagImplementationRetrieveRequest) -> operations.ExperimentsRequiresFlagImplementationRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/requires_flag_implementation/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsRequiresFlagImplementationRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    
    def experiments_results_retrieve(self, request: operations.ExperimentsResultsRetrieveRequest) -> operations.ExperimentsResultsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/{id}/results/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsResultsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    
    def experiments_retrieve(self, request: operations.ExperimentsRetrieveRequest) -> operations.ExperimentsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    
    def experiments_secondary_results_retrieve(self, request: operations.ExperimentsSecondaryResultsRetrieveRequest) -> operations.ExperimentsSecondaryResultsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/{id}/secondary_results/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsSecondaryResultsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    
    def experiments_update(self, request: operations.ExperimentsUpdateRequest) -> operations.ExperimentsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/experiments/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.ExperimentsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Experiment])
                res.experiment = out

        return res

    