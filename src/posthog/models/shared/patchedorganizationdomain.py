import dataclasses
from dataclasses_json import dataclass_json
from posthog import utils
from typing import Optional


@dataclass_json
@dataclasses.dataclass
class PatchedOrganizationDomainInput:
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('domain') }, 'form': { 'field_name': 'domain' }, 'multipart_form': { 'field_name': 'domain' }})
    jit_provisioning_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('jit_provisioning_enabled') }, 'form': { 'field_name': 'jit_provisioning_enabled' }, 'multipart_form': { 'field_name': 'jit_provisioning_enabled' }})
    saml_acs_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_acs_url') }, 'form': { 'field_name': 'saml_acs_url' }, 'multipart_form': { 'field_name': 'saml_acs_url' }})
    saml_entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_entity_id') }, 'form': { 'field_name': 'saml_entity_id' }, 'multipart_form': { 'field_name': 'saml_entity_id' }})
    saml_x509_cert: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('saml_x509_cert') }, 'form': { 'field_name': 'saml_x509_cert' }, 'multipart_form': { 'field_name': 'saml_x509_cert' }})
    sso_enforcement: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sso_enforcement') }, 'form': { 'field_name': 'sso_enforcement' }, 'multipart_form': { 'field_name': 'sso_enforcement' }})
    