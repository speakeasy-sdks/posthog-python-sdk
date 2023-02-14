import requests
from posthog.models import operations

class Prompts:
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

    
    def prompts_my_prompts_partial_update(self) -> operations.PromptsMyPromptsPartialUpdateResponse:
        r"""Create, read, update and delete prompt sequences state for a person.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/prompts/my_prompts/"
        
        
        client = self._client
        
        r = client.request("PATCH", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PromptsMyPromptsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    
    def prompts_my_prompts_partial_update(self) -> operations.PromptsMyPromptsPartialUpdateResponse:
        r"""Create, read, update and delete prompt sequences state for a person.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/api/prompts/my_prompts/"
        
        
        client = self._client
        
        r = client.request("PATCH", url)
        content_type = r.headers.get("Content-Type")

        res = operations.PromptsMyPromptsPartialUpdateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            pass

        return res

    