from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class PromptsMyPromptsPartialUpdateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    