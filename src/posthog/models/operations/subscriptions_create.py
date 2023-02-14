import dataclasses
from ..shared import subscription as shared_subscription
from typing import Optional


@dataclasses.dataclass
class SubscriptionsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SubscriptionsCreateRequests:
    subscription: Optional[shared_subscription.SubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    subscription1: Optional[shared_subscription.SubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    subscription2: Optional[shared_subscription.SubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class SubscriptionsCreateRequest:
    path_params: SubscriptionsCreatePathParams = dataclasses.field()
    request: SubscriptionsCreateRequests = dataclasses.field()
    

@dataclasses.dataclass
class SubscriptionsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    