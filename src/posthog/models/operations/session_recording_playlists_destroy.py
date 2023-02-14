import dataclasses



@dataclasses.dataclass
class SessionRecordingPlaylistsDestroyPathParams:
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    short_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'short_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class SessionRecordingPlaylistsDestroyRequest:
    path_params: SessionRecordingPlaylistsDestroyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class SessionRecordingPlaylistsDestroyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    