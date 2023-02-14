import dataclasses
from ..shared import paginatedteambasiclist as shared_paginatedteambasiclist
from typing import Optional


@dataclasses.dataclass
class ListQueryParams:
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class ListRequest:
    query_params: ListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class ListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_team_basic_list: Optional[shared_paginatedteambasiclist.PaginatedTeamBasicList] = dataclasses.field(default=None)
    