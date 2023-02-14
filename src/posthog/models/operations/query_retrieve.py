import dataclasses
from typing import Optional


@dataclasses.dataclass
class QueryRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class QueryRetrieveQueryParams:
    query: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'query', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class QueryRetrieveRequest:
    path_params: QueryRetrievePathParams = dataclasses.field()
    query_params: QueryRetrieveQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class QueryRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    