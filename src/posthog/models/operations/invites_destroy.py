import dataclasses



@dataclasses.dataclass
class InvitesDestroyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class InvitesDestroyRequest:
    path_params: InvitesDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class InvitesDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    