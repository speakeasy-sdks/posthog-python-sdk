from __future__ import annotations
import dataclasses
from ..shared import subscription as shared_subscription
from typing import Optional


@dataclasses.dataclass
class SubscriptionsUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SubscriptionsUpdateRequests:
    subscription: Optional[shared_subscription.SubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    subscription1: Optional[shared_subscription.SubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    subscription2: Optional[shared_subscription.SubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class SubscriptionsUpdateRequest:
    path_params: SubscriptionsUpdatePathParams = dataclasses.field()
    request: SubscriptionsUpdateRequests = dataclasses.field()
    

@dataclasses.dataclass
class SubscriptionsUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    