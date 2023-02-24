from __future__ import annotations
import dataclasses
from ..shared import sessionrecordingplaylist as shared_sessionrecordingplaylist
from typing import Optional


@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsCreatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    session_recording_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'session_recording_id', 'style': 'simple', 'explode': False }})
    short_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'short_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsCreateRequests:
    session_recording_playlist: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    session_recording_playlist1: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    session_recording_playlist2: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsCreateRequest:
    path_params: SessionRecordingPlaylistsRecordingsCreatePathParams = dataclasses.field()
    request: Optional[SessionRecordingPlaylistsRecordingsCreateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    session_recording_playlist: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylist] = dataclasses.field(default=None)
    