import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class Organizations:
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
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
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
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
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
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
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
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DomainsVerifyCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationDomain])
                res.organization_domain = out

        return res

    
    def invites_bulk_create(self, request: operations.InvitesBulkCreateRequest) -> operations.InvitesBulkCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/invites/bulk/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.InvitesBulkCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationInvite])
                res.organization_invite = out

        return res

    
    def invites_create(self, request: operations.InvitesCreateRequest) -> operations.InvitesCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/invites/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = self._client
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.InvitesCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationInvite])
                res.organization_invite = out

        return res

    
    def invites_destroy(self, request: operations.InvitesDestroyRequest) -> operations.InvitesDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/invites/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.InvitesDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def invites_list(self, request: operations.InvitesListRequest) -> operations.InvitesListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/invites/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.InvitesListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedOrganizationInviteList])
                res.paginated_organization_invite_list = out

        return res

    
    def members_destroy(self, request: operations.MembersDestroyRequest) -> operations.MembersDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/members/{user__uuid}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.MembersDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def members_list(self, request: operations.MembersListRequest) -> operations.MembersListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/members/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.MembersListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedOrganizationMemberList])
                res.paginated_organization_member_list = out

        return res

    
    def members_partial_update(self, request: operations.MembersPartialUpdateRequest) -> operations.MembersPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/members/{user__uuid}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.MembersPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationMember])
                res.organization_member = out

        return res

    
    def members_update(self, request: operations.MembersUpdateRequest) -> operations.MembersUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/organizations/{parent_lookup_organization_id}/members/{user__uuid}/", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PUT", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.MembersUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.OrganizationMember])
                res.organization_member = out

        return res

    
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

    