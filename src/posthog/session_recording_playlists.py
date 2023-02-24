import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class SessionRecordingPlaylists:
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

    
    def session_recording_playlists_create(self, request: operations.SessionRecordingPlaylistsCreateRequest) -> operations.SessionRecordingPlaylistsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SessionRecordingPlaylist])
                res.session_recording_playlist = out

        return res

    
    def session_recording_playlists_destroy(self, request: operations.SessionRecordingPlaylistsDestroyRequest) -> operations.SessionRecordingPlaylistsDestroyResponse:
        r"""Hard delete of this model is not allowed. Use a patch API call to set \"deleted\" to true
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 405:
            pass

        return res

    
    def session_recording_playlists_list(self, request: operations.SessionRecordingPlaylistsListRequest) -> operations.SessionRecordingPlaylistsListResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = self._client
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsListResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.PaginatedSessionRecordingPlaylistList])
                res.paginated_session_recording_playlist_list = out

        return res

    
    def session_recording_playlists_partial_update(self, request: operations.SessionRecordingPlaylistsPartialUpdateRequest) -> operations.SessionRecordingPlaylistsPartialUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PATCH", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SessionRecordingPlaylist])
                res.session_recording_playlist = out

        return res

    
    def session_recording_playlists_recordings_create(self, request: operations.SessionRecordingPlaylistsRecordingsCreateRequest) -> operations.SessionRecordingPlaylistsRecordingsCreateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("POST", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsRecordingsCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SessionRecordingPlaylist])
                res.session_recording_playlist = out

        return res

    
    def session_recording_playlists_recordings_destroy(self, request: operations.SessionRecordingPlaylistsRecordingsDestroyRequest) -> operations.SessionRecordingPlaylistsRecordingsDestroyResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/{session_recording_id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsRecordingsDestroyResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 204:
            pass

        return res

    
    def session_recording_playlists_recordings_retrieve(self, request: operations.SessionRecordingPlaylistsRecordingsRetrieveRequest) -> operations.SessionRecordingPlaylistsRecordingsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/recordings/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsRecordingsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SessionRecordingPlaylist])
                res.session_recording_playlist = out

        return res

    
    def session_recording_playlists_retrieve(self, request: operations.SessionRecordingPlaylistsRetrieveRequest) -> operations.SessionRecordingPlaylistsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SessionRecordingPlaylist])
                res.session_recording_playlist = out

        return res

    
    def session_recording_playlists_update(self, request: operations.SessionRecordingPlaylistsUpdateRequest) -> operations.SessionRecordingPlaylistsUpdateResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recording_playlists/{short_id}/", request.path_params)
        
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = self._client
        
        r = client.request("PUT", url, data=data, files=form, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingPlaylistsUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.SessionRecordingPlaylist])
                res.session_recording_playlist = out

        return res

    