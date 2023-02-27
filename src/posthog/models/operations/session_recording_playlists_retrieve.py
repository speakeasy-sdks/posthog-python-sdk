from __future__ import annotations
import dataclasses
from ..shared import sessionrecordingplaylist as shared_sessionrecordingplaylist
from typing import Optional


@dataclasses.dataclass
class SessionRecordingPlaylistsRetrievePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    short_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'short_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRetrieveRequest:
    path_params: SessionRecordingPlaylistsRetrievePathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRetrieveResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    session_recording_playlist: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylist] = dataclasses.field(default=None)
    