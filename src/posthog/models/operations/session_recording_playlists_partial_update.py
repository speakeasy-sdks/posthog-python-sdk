import dataclasses
from ..shared import patchedsessionrecordingplaylist as shared_patchedsessionrecordingplaylist
from ..shared import sessionrecordingplaylist as shared_sessionrecordingplaylist
from typing import Optional


@dataclasses.dataclass
class SessionRecordingPlaylistsPartialUpdatePathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    short_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'short_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsPartialUpdateRequests:
    patched_session_recording_playlist: Optional[shared_patchedsessionrecordingplaylist.PatchedSessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    patched_session_recording_playlist1: Optional[shared_patchedsessionrecordingplaylist.PatchedSessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/x-www-form-urlencoded' }})
    patched_session_recording_playlist2: Optional[shared_patchedsessionrecordingplaylist.PatchedSessionRecordingPlaylistInput] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'multipart/form-data' }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsPartialUpdateRequest:
    path_params: SessionRecordingPlaylistsPartialUpdatePathParams = dataclasses.field()
    request: Optional[SessionRecordingPlaylistsPartialUpdateRequests] = dataclasses.field(default=None)
    

@dataclasses.dataclass
class SessionRecordingPlaylistsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    session_recording_playlist: Optional[shared_sessionrecordingplaylist.SessionRecordingPlaylist] = dataclasses.field(default=None)
    