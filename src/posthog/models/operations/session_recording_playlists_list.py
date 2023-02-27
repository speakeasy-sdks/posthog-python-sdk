from __future__ import annotations
import dataclasses
from ..shared import paginatedsessionrecordingplaylistlist as shared_paginatedsessionrecordingplaylistlist
from typing import Optional


@dataclasses.dataclass
class SessionRecordingPlaylistsListPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsListQueryParams:
    created_by: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created_by', 'style': 'form', 'explode': True }})
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    offset: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    short_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'short_id', 'style': 'form', 'explode': True }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsListRequest:
    path_params: SessionRecordingPlaylistsListPathParams = dataclasses.field()
    query_params: SessionRecordingPlaylistsListQueryParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingPlaylistsListResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    paginated_session_recording_playlist_list: Optional[shared_paginatedsessionrecordingplaylistlist.PaginatedSessionRecordingPlaylistList] = dataclasses.field(default=None)
    