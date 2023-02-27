import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class FeatureFlags:
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

    
    def feature_flags_activity_retrieve(self, request: operations.FeatureFlagsActivityRetrieveRequest) -> operations.FeatureFlagsActivityRetrieveResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/activity/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsActivityRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_activity_retrieve_2(self, request: operations.FeatureFlagsActivityRetrieve2Request) -> operations.FeatureFlagsActivityRetrieve2Response:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{id}/activity/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsActivityRetrieve2Response(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_create(self, request: operations.FeatureFlagsCreateRequest) -> operations.FeatureFlagsCreateResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_destroy(self, request: operations.FeatureFlagsDestroyRequest) -> operations.FeatureFlagsDestroyResponse:
        r"""Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 405:
            pass

        return res

    
    def feature_flags_evaluation_reasons_retrieve(self, request: operations.FeatureFlagsEvaluationReasonsRetrieveRequest) -> operations.FeatureFlagsEvaluationReasonsRetrieveResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/evaluation_reasons/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsEvaluationReasonsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_list(self, request: operations.FeatureFlagsListRequest) -> operations.FeatureFlagsListResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedFeatureFlagList])
                res.paginated_feature_flag_list = out

        return res

    
    def feature_flags_local_evaluation_retrieve(self, request: operations.FeatureFlagsLocalEvaluationRetrieveRequest) -> operations.FeatureFlagsLocalEvaluationRetrieveResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/local_evaluation/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsLocalEvaluationRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_my_flags_retrieve(self, request: operations.FeatureFlagsMyFlagsRetrieveRequest) -> operations.FeatureFlagsMyFlagsRetrieveResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/my_flags/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsMyFlagsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_partial_update(self, request: operations.FeatureFlagsPartialUpdateRequest) -> operations.FeatureFlagsPartialUpdateResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_retrieve(self, request: operations.FeatureFlagsRetrieveRequest) -> operations.FeatureFlagsRetrieveResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_role_access_create(self, request: operations.FeatureFlagsRoleAccessCreateRequest) -> operations.FeatureFlagsRoleAccessCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{parent_lookup_feature_flag_id}/role_access/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsRoleAccessCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlagRoleAccessOutput])
                res.feature_flag_role_access = out

        return res

    
    def feature_flags_role_access_destroy(self, request: operations.FeatureFlagsRoleAccessDestroyRequest) -> operations.FeatureFlagsRoleAccessDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{parent_lookup_feature_flag_id}/role_access/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsRoleAccessDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def feature_flags_role_access_list(self, request: operations.FeatureFlagsRoleAccessListRequest) -> operations.FeatureFlagsRoleAccessListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{parent_lookup_feature_flag_id}/role_access/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsRoleAccessListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedFeatureFlagRoleAccessList])
                res.paginated_feature_flag_role_access_list = out

        return res

    
    def feature_flags_role_access_retrieve(self, request: operations.FeatureFlagsRoleAccessRetrieveRequest) -> operations.FeatureFlagsRoleAccessRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{parent_lookup_feature_flag_id}/role_access/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsRoleAccessRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlagRoleAccessOutput])
                res.feature_flag_role_access = out

        return res

    
    def feature_flags_update(self, request: operations.FeatureFlagsUpdateRequest) -> operations.FeatureFlagsUpdateResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/{id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    
    def feature_flags_user_blast_radius_create(self, request: operations.FeatureFlagsUserBlastRadiusCreateRequest) -> operations.FeatureFlagsUserBlastRadiusCreateResponse:
        r"""Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.
        
        If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/feature_flags/user_blast_radius/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and form is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.FeatureFlagsUserBlastRadiusCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.FeatureFlag])
                res.feature_flag = out

        return res

    