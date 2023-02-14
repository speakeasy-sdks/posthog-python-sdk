<!-- Start SDK Example Usage -->
```python
import posthog
from posthog.models import operations, shared

s = posthog.PostHog()
   
req = operations.ActionsCountRetrieveRequest(
    path_params=operations.ActionsCountRetrievePathParams(
        id=548814,
        project_id="deserunt",
    ),
    query_params=operations.ActionsCountRetrieveQueryParams(
        format="undefined",
    ),
)
    
res = s.actions.actions_count_retrieve(req)

if res.action is not None:
    # handle response
```
<!-- End SDK Example Usage -->