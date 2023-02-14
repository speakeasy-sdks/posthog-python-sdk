import requests
from . import utils
from posthog.models import operations

class UploadedMedia:
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

    
    def uploaded_media_create(self, request: operations.UploadedMediaCreateRequest) -> operations.UploadedMediaCreateResponse:
        r"""
            When object storage is available this API allows upload of media which can be used, for example, in text cards on dashboards.
        
            Uploaded media must have a content type beginning with 'image/' and be less than 4MB.
            
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{project_id}/uploaded_media/", request.path_params)
        
        
        client = self._client
        
        r = client.request("POST", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UploadedMediaCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            pass

        return res

    