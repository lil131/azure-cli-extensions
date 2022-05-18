# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

MAXIMUM_SECRET_LENGTH = 20
MAXIMUM_CONTAINER_APP_NAME_LENGTH = 40

SHORT_POLLING_INTERVAL_SECS = 3
LONG_POLLING_INTERVAL_SECS = 10

LOG_ANALYTICS_RP = "Microsoft.OperationalInsights"

MAX_ENV_PER_LOCATION = 2

MICROSOFT_SECRET_SETTING_NAME = "MICROSOFT_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
FACEBOOK_SECRET_SETTING_NAME = "FACEBOOK_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
GITHUB_SECRET_SETTING_NAME = "GITHUB_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
GOOGLE_SECRET_SETTING_NAME = "GOOGLE_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
MSA_SECRET_SETTING_NAME = "MSA_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
TWITTER_SECRET_SETTING_NAME = "TWITTER_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
APPLE_SECRET_SETTING_NAME = "APPLE_PROVIDER_AUTHENTICATION_SECRET".lower().replace("_", "-")
TRUE_STRING = "true"
FALSE_STRING = "false"