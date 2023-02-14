import dataclasses



@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsDestroyPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    session_recording_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'session_recording_id', 'style': 'simple', 'explode': False }})
    short_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'short_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsDestroyRequest:
    path_params: SessionRecordingPlaylistsRecordingsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingPlaylistsRecordingsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    