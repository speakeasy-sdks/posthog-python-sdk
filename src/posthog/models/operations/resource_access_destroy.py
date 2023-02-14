import dataclasses



@dataclasses.dataclass
class ResourceAccessDestroyPathParams:
    id: int = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    parent_lookup_organization_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'parent_lookup_organization_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ResourceAccessDestroyRequest:
    path_params: ResourceAccessDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class ResourceAccessDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    