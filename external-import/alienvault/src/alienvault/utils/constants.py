# -*- coding: utf-8 -*-
"""threatlens AlienVault utilities constants module."""

from stix2 import TLP_AMBER, TLP_GREEN, TLP_RED, TLP_WHITE  # type: ignore

TLP_MARKING_DEFINITION_MAPPING = {
    "white": TLP_WHITE,
    "green": TLP_GREEN,
    "amber": TLP_AMBER,
    "red": TLP_RED,
}

DEFAULT_TLP_MARKING_DEFINITION = TLP_WHITE


X_THREATLENS_ALIASES = "x_threatlens_aliases"
X_THREATLENS_ORGANIZATION_TYPE = "x_threatlens_organization_type"
X_THREATLENS_RELIABILITY = "x_threatlens_reliability"
X_THREATLENS_LOCATION_TYPE = "x_threatlens_location_type"
X_MITRE_ID = "x_mitre_id"
X_THREATLENS_REPORT_STATUS = "x_threatlens_report_status"
X_THREATLENS_SCORE = "x_threatlens_score"
X_THREATLENS_LABELS = "x_threatlens_labels"
X_THREATLENS_CREATED_BY_REF = "x_threatlens_created_by_ref"
X_THREATLENS_MAIN_OBSERVABLE_TYPE = "x_threatlens_main_observable_type"
