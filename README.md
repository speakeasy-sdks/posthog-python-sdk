# PostHog Python SDK

<div align="left">
   <p>The PostHog API allows you to perform any action as if you were an authenticated user utilizing the PostHog UI. It is mostly used for getting data out of PostHog, as well as other private actions such as creating a feature flag.</p>
   <a href="https://github.com/speakeasy-sdks/posthog-python-sdk/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/posthog-python-sdk/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
   <a href="https://posthog.com/docs/api"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="[https://discord.com/channels/1065392526745403502/1065392527198404670](https://posthog.com/slack)"><img src="https://img.shields.io/static/v1?label=Slack&message=Join&color=7289da&style=for-the-badge" /></a>
</div>


<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install posthog
```
<!-- End SDK Installation -->

## Authentication

Personal API keys allow full access to your account, just like e-mail address and password, but you can create any number of them and each one can invalidated individually at any moment. This makes for greater control for you and improved security of stored data.

1. How to obtain a personal API key
2. Click on your name/avatar on the top right.
3. Click the gear next to your name to access 'Account settings'.
4. Navigate to the 'Personal API Keys' section.
5. Click "+ Create a Personal API Key".
6. Give your new key a label – it's just for you, usually to describe the key's purpose.
7. Click 'Create Key'.

There you go! At the top of the list you should now be seeing your brand new key. Immediately copy its value, as you'll never see it again after refreshing the page. But don't worry if you forget to copy it – you can delete and create keys as much as you want.

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import posthog
from posthog.models import operations, shared

s = posthog.PostHog()
   
req = operations.ActionsCountRetrieveRequest(
    path_params=operations.ActionsCountRetrievePathParams(
        id=548814,
        project_id="deserunt",
    ),
    query_params=operations.ActionsCountRetrieveQueryParams(
        format="undefined",
    ),
)
    
res = s.actions.actions_count_retrieve(req)

if res.action is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## SDK Available Operations


### actions

* `actions_count_retrieve`
* `actions_create`
* `actions_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `actions_list`
* `actions_partial_update`
* `actions_people_retrieve`
* `actions_retrieve`
* `actions_update`

### activity_log

* `activity_log_bookmark_activity_notification_create`
* `activity_log_important_changes_retrieve`

### annotations

* `annotations_create` - Create, Read, Update and Delete annotations. [See docs](https://posthog.com/docs/user-guides/annotations) for more information on annotations.
* `annotations_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `annotations_list` - Create, Read, Update and Delete annotations. [See docs](https://posthog.com/docs/user-guides/annotations) for more information on annotations.
* `annotations_partial_update` - Create, Read, Update and Delete annotations. [See docs](https://posthog.com/docs/user-guides/annotations) for more information on annotations.
* `annotations_retrieve` - Create, Read, Update and Delete annotations. [See docs](https://posthog.com/docs/user-guides/annotations) for more information on annotations.
* `annotations_update` - Create, Read, Update and Delete annotations. [See docs](https://posthog.com/docs/user-guides/annotations) for more information on annotations.

### app_metrics

* `app_metrics_error_details_retrieve`
* `app_metrics_historical_exports_retrieve`
* `app_metrics_historical_exports_retrieve_2`
* `app_metrics_retrieve`

### cohorts

* `cohorts_create`
* `cohorts_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `cohorts_list`
* `cohorts_partial_update`
* `cohorts_persons_retrieve`
* `cohorts_retrieve`
* `cohorts_update`

### dashboard_templates

* `dashboard_templates_create`
* `dashboard_templates_repository_retrieve`

### dashboards

* `dashboards_create`
* `dashboards_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `dashboards_list`
* `dashboards_move_tile_partial_update`
* `dashboards_partial_update`
* `dashboards_retrieve`
* `dashboards_update`

### domains

* `domains_create`
* `domains_destroy`
* `domains_list`
* `domains_partial_update`
* `domains_retrieve`
* `domains_update`
* `domains_verify_create`

### event_definitions

* `event_definitions_list`
* `event_definitions_partial_update`
* `event_definitions_retrieve`
* `event_definitions_update`

### events

* `events_retrieve`
* `events_values_retrieve`

### experiments

* `experiments_create`
* `experiments_destroy`
* `experiments_list`
* `experiments_partial_update`
* `experiments_requires_flag_implementation_retrieve`
* `experiments_results_retrieve`
* `experiments_retrieve`
* `experiments_secondary_results_retrieve`
* `experiments_update`

### exports

* `exports_content_retrieve`
* `exports_create`
* `exports_retrieve`

### feature_flags

* `feature_flags_activity_retrieve` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_activity_retrieve_2` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_create` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `feature_flags_evaluation_reasons_retrieve` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_list` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_local_evaluation_retrieve` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_my_flags_retrieve` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_partial_update` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_retrieve` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_role_access_create`
* `feature_flags_role_access_destroy`
* `feature_flags_role_access_list`
* `feature_flags_role_access_retrieve`
* `feature_flags_update` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.
* `feature_flags_user_blast_radius_create` - Create, read, update and delete feature flags. [See docs](https://posthog.com/docs/user-guides/feature-flags) for more information on feature flags.

If you're looking to use feature flags on your application, you can either use our JavaScript Library or our dedicated endpoint to check if feature flags are enabled for a given user.

### funnel

* `funnels`

### groups

* `groups_find_retrieve`
* `groups_list`
* `groups_property_definitions_retrieve`
* `groups_property_values_retrieve`
* `groups_related_retrieve`

### groups_types

* `groups_types_list`
* `groups_types_update_metadata_partial_update`

### hooks

* `hooks_create` - Retrieve, create, update or destroy REST hooks.
* `hooks_destroy` - Retrieve, create, update or destroy REST hooks.
* `hooks_list` - Retrieve, create, update or destroy REST hooks.
* `hooks_partial_update` - Retrieve, create, update or destroy REST hooks.
* `hooks_retrieve` - Retrieve, create, update or destroy REST hooks.
* `hooks_update` - Retrieve, create, update or destroy REST hooks.

### ingestion_warnings

* `ingestion_warnings_retrieve`

### insights

* `funnels`
* `trends`
* `insights_activity_retrieve`
* `insights_activity_retrieve_2`
* `insights_cancel_create`
* `insights_create`
* `insights_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `insights_funnel_correlation_create`
* `insights_funnel_correlation_retrieve`
* `insights_funnel_retrieve`
* `insights_list`
* `insights_my_last_viewed_retrieve` - Returns basic details about the last 5 insights viewed by this user. Most recently viewed first.
* `insights_partial_update`
* `insights_path_create`
* `insights_path_retrieve`
* `insights_retention_retrieve`
* `insights_retrieve`
* `insights_timing_create`
* `insights_trend_retrieve`
* `insights_update`
* `insights_viewed_create`

### integrations

* `integrations_channels_retrieve`
* `integrations_create`
* `integrations_destroy`
* `integrations_list`
* `integrations_retrieve`

### invites

* `invites_bulk_create`
* `invites_create`
* `invites_destroy`
* `invites_list`

### is_generating_demo_data

* `is_generating_demo_data_retrieve` - Projects for the current organization.

### members

* `members_destroy`
* `members_list`
* `members_partial_update`
* `members_update`

### organizations

* `domains_create`
* `domains_destroy`
* `domains_list`
* `domains_partial_update`
* `domains_retrieve`
* `domains_update`
* `domains_verify_create`
* `invites_bulk_create`
* `invites_create`
* `invites_destroy`
* `invites_list`
* `members_destroy`
* `members_list`
* `members_partial_update`
* `members_update`
* `plugins_activity_retrieve`
* `plugins_check_for_updates_retrieve`
* `plugins_create`
* `plugins_destroy`
* `plugins_list`
* `plugins_partial_update`
* `plugins_repository_retrieve`
* `plugins_retrieve`
* `plugins_source_retrieve`
* `plugins_update`
* `plugins_update_source_partial_update`
* `plugins_upgrade_create`
* `resource_access_create`
* `resource_access_destroy`
* `resource_access_list`
* `resource_access_partial_update`
* `resource_access_retrieve`
* `resource_access_update`
* `roles_create`
* `roles_destroy`
* `roles_list`
* `roles_partial_update`
* `roles_retrieve`
* `roles_role_memberships_create`
* `roles_role_memberships_destroy`
* `roles_role_memberships_list`
* `roles_update`

### performance_events

* `performance_events_list`
* `performance_events_recent_pageviews_retrieve`

### persons

* `persons_activity_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_activity_retrieve_2` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_cohorts_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_delete_property_create` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_destroy` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_funnel_correlation_create` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_funnel_correlation_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_funnel_create` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_funnel_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_lifecycle_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_partial_update` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_path_create` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_path_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_properties_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_properties_timeline_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_retention_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_split_create` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_stickiness_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_trends_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_update` - Only for setting properties on the person. "properties" from the request data will be updated via a "$set" event.
This means that only the properties listed will be updated, but other properties won't be removed nor updated.
If you would like to remove a property use the `delete_property` endpoint.
* `persons_update_property_create` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.
* `persons_values_retrieve` - To create or update persons, use a PostHog library of your choice and [use an identify call](/docs/integrate/identifying-users). This API endpoint is only for reading and deleting.

### plugin_configs

* `plugin_configs_create`
* `plugin_configs_destroy`
* `plugin_configs_frontend_retrieve`
* `plugin_configs_job_create`
* `plugin_configs_list`
* `plugin_configs_logs_list`
* `plugin_configs_partial_update`
* `plugin_configs_rearrange_partial_update`
* `plugin_configs_retrieve`
* `plugin_configs_update`

### plugins

* `plugins_activity_retrieve`
* `plugins_check_for_updates_retrieve`
* `plugins_create`
* `plugins_destroy`
* `plugins_list`
* `plugins_partial_update`
* `plugins_repository_retrieve`
* `plugins_retrieve`
* `plugins_source_retrieve`
* `plugins_update`
* `plugins_update_source_partial_update`
* `plugins_upgrade_create`

### projects

* `create` - Projects for the current organization.
* `destroy` - Projects for the current organization.
* `list` - Projects for the current organization.
* `partial_update` - Projects for the current organization.
* `retrieve` - Projects for the current organization.
* `update` - Projects for the current organization.

### prompts

* `prompts_my_prompts_partial_update` - Create, read, update and delete prompt sequences state for a person.
* `prompts_my_prompts_partial_update` - Create, read, update and delete prompt sequences state for a person.

### property_definitions

* `property_definitions_list`
* `property_definitions_partial_update`
* `property_definitions_retrieve`
* `property_definitions_update`

### query

* `query_retrieve`

### reset_token

* `reset_token_partial_update` - Projects for the current organization.

### resource_access

* `resource_access_create`
* `resource_access_destroy`
* `resource_access_list`
* `resource_access_partial_update`
* `resource_access_retrieve`
* `resource_access_update`

### roles

* `roles_create`
* `roles_destroy`
* `roles_list`
* `roles_partial_update`
* `roles_retrieve`
* `roles_role_memberships_create`
* `roles_role_memberships_destroy`
* `roles_role_memberships_list`
* `roles_update`

### session_recording_playlists

* `session_recording_playlists_create`
* `session_recording_playlists_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `session_recording_playlists_list`
* `session_recording_playlists_partial_update`
* `session_recording_playlists_recordings_create`
* `session_recording_playlists_recordings_destroy`
* `session_recording_playlists_recordings_retrieve`
* `session_recording_playlists_retrieve`
* `session_recording_playlists_update`

### session_recordings

* `session_recordings_properties_retrieve`
* `session_recordings_retrieve`
* `session_recordings_retrieve_2`
* `session_recordings_snapshots_retrieve`

### subscriptions

* `subscriptions_create`
* `subscriptions_destroy` - Hard delete of this model is not allowed. Use a patch API call to set "deleted" to true
* `subscriptions_list`
* `subscriptions_partial_update`
* `subscriptions_retrieve`
* `subscriptions_update`

### tags

* `tags_list`

### trend

* `trends`

### uploaded_media

* `uploaded_media_create` - 
    When object storage is available this API allows upload of media which can be used, for example, in text cards on dashboards.

    Uploaded media must have a content type beginning with 'image/' and be less than 4MB.
    
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
