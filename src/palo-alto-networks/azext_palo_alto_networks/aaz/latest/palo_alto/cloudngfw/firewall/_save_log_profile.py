# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "palo-alto cloudngfw firewall save-log-profile",
)
class SaveLogProfile(AAZCommand):
    """Save Log Profile for Firewall

    :example: Save Log Profile for Firewall
        az palo-alto cloudngfw firewall save-log-profile --resource-group MyResourceGroup -n MyCloudngfwFirewall --log-option "SAME_DESTINATION" --log-type "TRAFFIC"
    """

    _aaz_info = {
        "version": "2022-08-29",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/paloaltonetworks.cloudngfw/firewalls/{}/savelogprofile", "2022-08-29"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return None

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.firewall_name = AAZStrArg(
            options=["-n", "--name", "--firewall-name"],
            help="Firewall resource name",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "LogSettings"

        _args_schema = cls._args_schema
        _args_schema.application_insights = AAZObjectArg(
            options=["--application-insights"],
            arg_group="LogSettings",
            help="Application Insight details",
        )
        _args_schema.common_destination = AAZObjectArg(
            options=["--common-destination"],
            arg_group="LogSettings",
            help="Common destination configurations",
        )
        cls._build_args_log_destination_create(_args_schema.common_destination)
        _args_schema.decrypt_log_destination = AAZObjectArg(
            options=["--decrypt-destination", "--decrypt-log-destination"],
            arg_group="LogSettings",
            help="Decrypt destination configurations",
        )
        cls._build_args_log_destination_create(_args_schema.decrypt_log_destination)
        _args_schema.log_option = AAZStrArg(
            options=["--log-option"],
            arg_group="LogSettings",
            help="Log option SAME/INDIVIDUAL",
            enum={"INDIVIDUAL_DESTINATION": "INDIVIDUAL_DESTINATION", "SAME_DESTINATION": "SAME_DESTINATION"},
        )
        _args_schema.log_type = AAZStrArg(
            options=["--log-type"],
            arg_group="LogSettings",
            help="One of possible log type",
            enum={"AUDIT": "AUDIT", "DECRYPTION": "DECRYPTION", "DLP": "DLP", "THREAT": "THREAT", "TRAFFIC": "TRAFFIC", "WILDFIRE": "WILDFIRE"},
        )
        _args_schema.threat_log_destination = AAZObjectArg(
            options=["--threat-destination", "--threat-log-destination"],
            arg_group="LogSettings",
            help="Threat destination configurations",
        )
        cls._build_args_log_destination_create(_args_schema.threat_log_destination)
        _args_schema.traffic_log_destination = AAZObjectArg(
            options=["--traffic-destination", "--traffic-log-destination"],
            arg_group="LogSettings",
            help="Traffic destination configurations",
        )
        cls._build_args_log_destination_create(_args_schema.traffic_log_destination)

        application_insights = cls._args_schema.application_insights
        application_insights.id = AAZStrArg(
            options=["id"],
            help="Resource id for Application Insights",
        )
        application_insights.key = AAZStrArg(
            options=["key"],
            help="Application Insights key",
        )
        return cls._args_schema

    _args_log_destination_create = None

    @classmethod
    def _build_args_log_destination_create(cls, _schema):
        if cls._args_log_destination_create is not None:
            _schema.event_hub_configurations = cls._args_log_destination_create.event_hub_configurations
            _schema.monitor_configurations = cls._args_log_destination_create.monitor_configurations
            _schema.storage_configurations = cls._args_log_destination_create.storage_configurations
            return

        cls._args_log_destination_create = AAZObjectArg()

        log_destination_create = cls._args_log_destination_create
        log_destination_create.event_hub_configurations = AAZObjectArg(
            options=["event-hub-configurations"],
            help="Event Hub configurations",
        )
        log_destination_create.monitor_configurations = AAZObjectArg(
            options=["monitor-configurations"],
            help="Monitor Log configurations",
        )
        log_destination_create.storage_configurations = AAZObjectArg(
            options=["storage-configurations"],
            help="Storage account configurations",
        )

        event_hub_configurations = cls._args_log_destination_create.event_hub_configurations
        event_hub_configurations.id = AAZStrArg(
            options=["id"],
            help="Resource ID of EventHub",
        )
        event_hub_configurations.name = AAZStrArg(
            options=["name"],
            help="EventHub name",
        )
        event_hub_configurations.name_space = AAZStrArg(
            options=["name-space"],
            help="EventHub namespace",
        )
        event_hub_configurations.policy_name = AAZStrArg(
            options=["policy-name"],
            help="EventHub policy name",
        )
        event_hub_configurations.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="Subscription Id",
        )

        monitor_configurations = cls._args_log_destination_create.monitor_configurations
        monitor_configurations.id = AAZStrArg(
            options=["id"],
            help="Resource ID of MonitorLog",
        )
        monitor_configurations.primary_key = AAZStrArg(
            options=["primary-key"],
            help="Primary Key value for Monitor",
        )
        monitor_configurations.secondary_key = AAZStrArg(
            options=["secondary-key"],
            help="Secondary Key value for Monitor",
        )
        monitor_configurations.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="Subscription Id",
        )
        monitor_configurations.workspace = AAZStrArg(
            options=["workspace"],
            help="MonitorLog workspace",
        )

        storage_configurations = cls._args_log_destination_create.storage_configurations
        storage_configurations.account_name = AAZStrArg(
            options=["account-name"],
            help="Storage account name",
        )
        storage_configurations.id = AAZStrArg(
            options=["id"],
            help="Resource ID of storage account",
        )
        storage_configurations.subscription_id = AAZStrArg(
            options=["subscription-id"],
            help="Subscription Id",
        )

        _schema.event_hub_configurations = cls._args_log_destination_create.event_hub_configurations
        _schema.monitor_configurations = cls._args_log_destination_create.monitor_configurations
        _schema.storage_configurations = cls._args_log_destination_create.storage_configurations

    def _execute_operations(self):
        self.pre_operations()
        self.FirewallsSaveLogProfile(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class FirewallsSaveLogProfile(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [204]:
                return self.on_204(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/PaloAltoNetworks.Cloudngfw/firewalls/{firewallName}/saveLogProfile",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "firewallName", self.ctx.args.firewall_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-08-29",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("applicationInsights", AAZObjectType, ".application_insights")
            _SaveLogProfileHelper._build_schema_log_destination_create(_builder.set_prop("commonDestination", AAZObjectType, ".common_destination"))
            _SaveLogProfileHelper._build_schema_log_destination_create(_builder.set_prop("decryptLogDestination", AAZObjectType, ".decrypt_log_destination"))
            _builder.set_prop("logOption", AAZStrType, ".log_option")
            _builder.set_prop("logType", AAZStrType, ".log_type")
            _SaveLogProfileHelper._build_schema_log_destination_create(_builder.set_prop("threatLogDestination", AAZObjectType, ".threat_log_destination"))
            _SaveLogProfileHelper._build_schema_log_destination_create(_builder.set_prop("trafficLogDestination", AAZObjectType, ".traffic_log_destination"))

            application_insights = _builder.get(".applicationInsights")
            if application_insights is not None:
                application_insights.set_prop("id", AAZStrType, ".id")
                application_insights.set_prop("key", AAZStrType, ".key")

            return self.serialize_content(_content_value)

        def on_204(self, session):
            pass


class _SaveLogProfileHelper:
    """Helper class for SaveLogProfile"""

    @classmethod
    def _build_schema_log_destination_create(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("eventHubConfigurations", AAZObjectType, ".event_hub_configurations")
        _builder.set_prop("monitorConfigurations", AAZObjectType, ".monitor_configurations")
        _builder.set_prop("storageConfigurations", AAZObjectType, ".storage_configurations")

        event_hub_configurations = _builder.get(".eventHubConfigurations")
        if event_hub_configurations is not None:
            event_hub_configurations.set_prop("id", AAZStrType, ".id")
            event_hub_configurations.set_prop("name", AAZStrType, ".name")
            event_hub_configurations.set_prop("nameSpace", AAZStrType, ".name_space")
            event_hub_configurations.set_prop("policyName", AAZStrType, ".policy_name")
            event_hub_configurations.set_prop("subscriptionId", AAZStrType, ".subscription_id")

        monitor_configurations = _builder.get(".monitorConfigurations")
        if monitor_configurations is not None:
            monitor_configurations.set_prop("id", AAZStrType, ".id")
            monitor_configurations.set_prop("primaryKey", AAZStrType, ".primary_key")
            monitor_configurations.set_prop("secondaryKey", AAZStrType, ".secondary_key")
            monitor_configurations.set_prop("subscriptionId", AAZStrType, ".subscription_id")
            monitor_configurations.set_prop("workspace", AAZStrType, ".workspace")

        storage_configurations = _builder.get(".storageConfigurations")
        if storage_configurations is not None:
            storage_configurations.set_prop("accountName", AAZStrType, ".account_name")
            storage_configurations.set_prop("id", AAZStrType, ".id")
            storage_configurations.set_prop("subscriptionId", AAZStrType, ".subscription_id")


__all__ = ["SaveLogProfile"]