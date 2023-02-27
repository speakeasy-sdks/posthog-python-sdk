from __future__ import annotations
import dataclasses
from ..shared import subscription as shared_subscription
from typing import Optional


@dataclasses.dataclass
class SubscriptionsRetrievePathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SubscriptionsRetrieveRequest:
    path_params: SubscriptionsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class SubscriptionsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    subscription: Optional[shared_subscription.Subscription] = dataclasses.field(default=None)
    