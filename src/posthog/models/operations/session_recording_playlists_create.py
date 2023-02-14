import dataclasses
from ..shared import sessionrecordingplaylist as shared_sessionrecordingplaylist
from typing import Optional


@dataclasses.dataclass
class SessionRecordingPlaylistsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsCreateRequests:
    session_recording_playlist: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    session_recording_playlist1: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    session_recording_playlist2: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsCreateRequest:
    path_params: SessionRecordingPlaylistsCreatePathParams = dataclasses.field()
    request: Optional[SessionRecordingPlaylistsCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class SessionRecordingPlaylistsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    session_recording_playlist: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylist] = dataclasses.field(default=None)
    