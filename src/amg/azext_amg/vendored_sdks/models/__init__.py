# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureMonitorWorkspaceIntegration
from ._models_py3 import EnterpriseConfigurations
from ._models_py3 import EnterpriseDetails
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import GrafanaConfigurations
from ._models_py3 import GrafanaIntegrations
from ._models_py3 import ManagedGrafana
from ._models_py3 import ManagedGrafanaListResponse
from ._models_py3 import ManagedGrafanaProperties
from ._models_py3 import ManagedGrafanaPropertiesUpdateParameters
from ._models_py3 import ManagedGrafanaUpdateParameters
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import MarketplaceTrialQuota
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import Resource
from ._models_py3 import ResourceSku
from ._models_py3 import SaasSubscriptionDetails
from ._models_py3 import Smtp
from ._models_py3 import SubscriptionTerm
from ._models_py3 import SystemData
from ._models_py3 import UserAssignedIdentity

from ._dashboard_management_client_enums import ActionType
from ._dashboard_management_client_enums import ApiKey
from ._dashboard_management_client_enums import AutoGeneratedDomainNameLabelScope
from ._dashboard_management_client_enums import AvailablePromotion
from ._dashboard_management_client_enums import CreatedByType
from ._dashboard_management_client_enums import DeterministicOutboundIP
from ._dashboard_management_client_enums import ManagedServiceIdentityType
from ._dashboard_management_client_enums import MarketplaceAutoRenew
from ._dashboard_management_client_enums import Origin
from ._dashboard_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._dashboard_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._dashboard_management_client_enums import ProvisioningState
from ._dashboard_management_client_enums import PublicNetworkAccess
from ._dashboard_management_client_enums import StartTLSPolicy
from ._dashboard_management_client_enums import ZoneRedundancy
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureMonitorWorkspaceIntegration",
    "EnterpriseConfigurations",
    "EnterpriseDetails",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "GrafanaConfigurations",
    "GrafanaIntegrations",
    "ManagedGrafana",
    "ManagedGrafanaListResponse",
    "ManagedGrafanaProperties",
    "ManagedGrafanaPropertiesUpdateParameters",
    "ManagedGrafanaUpdateParameters",
    "ManagedServiceIdentity",
    "MarketplaceTrialQuota",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "Resource",
    "ResourceSku",
    "SaasSubscriptionDetails",
    "Smtp",
    "SubscriptionTerm",
    "SystemData",
    "UserAssignedIdentity",
    "ActionType",
    "ApiKey",
    "AutoGeneratedDomainNameLabelScope",
    "AvailablePromotion",
    "CreatedByType",
    "DeterministicOutboundIP",
    "ManagedServiceIdentityType",
    "MarketplaceAutoRenew",
    "Origin",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "StartTLSPolicy",
    "ZoneRedundancy",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
