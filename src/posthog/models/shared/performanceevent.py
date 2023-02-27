from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from posthog import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PerformanceEvent:
    current_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('current_url') }})
    distinct_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('distinct_id') }})
    entry_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('entry_type') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    session_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('session_id') }})
    time_origin: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('time_origin'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    timestamp: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('timestamp'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    uuid: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('uuid') }})
    window_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('window_id') }})
    connect_end: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connect_end'), 'exclude': lambda f: f is None }})
    connect_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('connect_start'), 'exclude': lambda f: f is None }})
    decoded_body_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('decoded_body_size'), 'exclude': lambda f: f is None }})
    dom_complete: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dom_complete'), 'exclude': lambda f: f is None }})
    dom_content_loaded_event: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dom_content_loaded_event'), 'exclude': lambda f: f is None }})
    dom_interactive: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dom_interactive'), 'exclude': lambda f: f is None }})
    domain_lookup_end: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('domain_lookup_end'), 'exclude': lambda f: f is None }})
    domain_lookup_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('domain_lookup_start'), 'exclude': lambda f: f is None }})
    duration: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('duration'), 'exclude': lambda f: f is None }})
    encoded_body_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('encoded_body_size'), 'exclude': lambda f: f is None }})
    fetch_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('fetch_start'), 'exclude': lambda f: f is None }})
    initiator_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('initiator_type'), 'exclude': lambda f: f is None }})
    largest_contentful_paint_element: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('largest_contentful_paint_element'), 'exclude': lambda f: f is None }})
    largest_contentful_paint_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('largest_contentful_paint_id'), 'exclude': lambda f: f is None }})
    largest_contentful_paint_load_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('largest_contentful_paint_load_time'), 'exclude': lambda f: f is None }})
    largest_contentful_paint_render_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('largest_contentful_paint_render_time'), 'exclude': lambda f: f is None }})
    largest_contentful_paint_size: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('largest_contentful_paint_size'), 'exclude': lambda f: f is None }})
    largest_contentful_paint_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('largest_contentful_paint_url'), 'exclude': lambda f: f is None }})
    load_event_end: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('load_event_end'), 'exclude': lambda f: f is None }})
    load_event_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('load_event_start'), 'exclude': lambda f: f is None }})
    navigation_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('navigation_type'), 'exclude': lambda f: f is None }})
    next_hop_protocol: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('next_hop_protocol'), 'exclude': lambda f: f is None }})
    pageview_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pageview_id'), 'exclude': lambda f: f is None }})
    redirect_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirect_count'), 'exclude': lambda f: f is None }})
    redirect_end: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirect_end'), 'exclude': lambda f: f is None }})
    redirect_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('redirect_start'), 'exclude': lambda f: f is None }})
    render_blocking_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_blocking_status'), 'exclude': lambda f: f is None }})
    request_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('request_start'), 'exclude': lambda f: f is None }})
    response_end: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('response_end'), 'exclude': lambda f: f is None }})
    response_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('response_start'), 'exclude': lambda f: f is None }})
    response_status: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('response_status'), 'exclude': lambda f: f is None }})
    secure_connection_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('secure_connection_start'), 'exclude': lambda f: f is None }})
    start_time: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('start_time'), 'exclude': lambda f: f is None }})
    transfer_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('transfer_size'), 'exclude': lambda f: f is None }})
    unload_event_end: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unload_event_end'), 'exclude': lambda f: f is None }})
    unload_event_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('unload_event_start'), 'exclude': lambda f: f is None }})
    worker_start: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('worker_start'), 'exclude': lambda f: f is None }})
    