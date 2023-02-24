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
class OrganizationDomainInput:
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('domain') }, 'form': { 'field_name': 'domain' }, 'multipart_form': { 'field_name': 'domain' }})
    jit_provisioning_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('jit_provisioning_enabled'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'jit_provisioning_enabled' }, 'multipart_form': { 'field_name': 'jit_provisioning_enabled' }})
    saml_acs_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_acs_url'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'saml_acs_url' }, 'multipart_form': { 'field_name': 'saml_acs_url' }})
    saml_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_entity_id'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'saml_entity_id' }, 'multipart_form': { 'field_name': 'saml_entity_id' }})
    saml_x509_cert: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_x509_cert'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'saml_x509_cert' }, 'multipart_form': { 'field_name': 'saml_x509_cert' }})
    sso_enforcement: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sso_enforcement'), 'exclude': lambda f: f is None }, 'form': { 'field_name': 'sso_enforcement' }, 'multipart_form': { 'field_name': 'sso_enforcement' }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationDomain:
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('domain') }})
    has_saml: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('has_saml') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    is_verified: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_verified') }})
    verification_challenge: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('verification_challenge') }})
    verified_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('verified_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    jit_provisioning_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('jit_provisioning_enabled'), 'exclude': lambda f: f is None }})
    saml_acs_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_acs_url'), 'exclude': lambda f: f is None }})
    saml_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_entity_id'), 'exclude': lambda f: f is None }})
    saml_x509_cert: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_x509_cert'), 'exclude': lambda f: f is None }})
    sso_enforcement: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sso_enforcement'), 'exclude': lambda f: f is None }})
    