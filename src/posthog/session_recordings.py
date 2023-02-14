import requests
from . import utils
from posthog.models import operations

class SessionRecordings:
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

    
    def session_recordings_properties_retrieve(self, request: operations.SessionRecordingsPropertiesRetrieveRequest) -> operations.SessionRecordingsPropertiesRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recordings/properties/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingsPropertiesRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def session_recordings_retrieve(self, request: operations.SessionRecordingsRetrieveRequest) -> operations.SessionRecordingsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recordings/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def session_recordings_retrieve_2(self, request: operations.SessionRecordingsRetrieve2Request) -> operations.SessionRecordingsRetrieve2Response:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recordings/{id}/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingsRetrieve2Response(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def session_recordings_snapshots_retrieve(self, request: operations.SessionRecordingsSnapshotsRetrieveRequest) -> operations.SessionRecordingsSnapshotsRetrieveResponse:
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/session_recordings/{id}/snapshots/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.SessionRecordingsSnapshotsRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    