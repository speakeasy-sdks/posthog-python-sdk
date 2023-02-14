import dataclasses



@dataclasses.dataclass
class RolesDestroyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RolesDestroyRequest:
    path_params: RolesDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RolesDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    