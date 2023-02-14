import requests
from . import utils
from posthog.models import operations, shared
from typing import Optional

class IsGeneratingDemoData:
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

    
    def is_generating_demo_data_retrieve(self, request: operations.IsGeneratingDemoDataRetrieveRequest) -> operations.IsGeneratingDemoDataRetrieveResponse:
        r"""Projects for the current organization.
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/api/projects/{id}/is_generating_demo_data/", request.path_params)
        
        
        client = self._client
        
        r = client.request("GET", url)
        content_type = r.headers.get("Content-Type")

        res = operations.IsGeneratingDemoDataRetrieveResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Team])
                res.team = out

        return res

    