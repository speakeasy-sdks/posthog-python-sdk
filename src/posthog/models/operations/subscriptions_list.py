from __future__ import annotations
import dataclasses
from ..shared import paginatedsubscriptionlist as shared_paginatedsubscriptionlist
from typing import Optional


@dataclasses.dataclass
class SubscriptionsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SubscriptionsListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SubscriptionsListRequest:
    path_params: SubscriptionsListPathParams = dataclasses.field()
    query_params: SubscriptionsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class SubscriptionsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_subscription_list: Optional[shared_paginatedsubscriptionlist.PaginatedSubscriptionList] = dataclasses.field(default=None)
    