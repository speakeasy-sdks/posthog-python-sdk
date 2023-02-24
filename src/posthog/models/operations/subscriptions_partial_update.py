from __future__ import annotations
import dataclasses
from ..shared import patchedsubscription as shared_patchedsubscription
from ..shared import subscription as shared_subscription
from typing import Optional


@dataclasses.dataclass
class SubscriptionsPartialUpdatePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SubscriptionsPartialUpdateRequests:
    patched_subscription: Optional[shared_patchedsubscription.PatchedSubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_subscription1: Optional[shared_patchedsubscription.PatchedSubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_subscription2: Optional[shared_patchedsubscription.PatchedSubscriptionInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class SubscriptionsPartialUpdateRequest:
    path_params: SubscriptionsPartialUpdatePathParams = dataclasses.field()
    request: Optional[SubscriptionsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class SubscriptionsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    