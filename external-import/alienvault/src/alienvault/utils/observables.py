# -*- coding: utf-8 -*-
"""threatlens AlienVault observable utilities module."""

from typing import Any, List, Mapping, NamedTuple, Optional

from alienvault.utils.constants import (
    X_THREATLENS_CREATED_BY_REF,
    X_THREATLENS_LABELS,
    X_THREATLENS_SCORE,
)
from pycti import CustomObservableCryptocurrencyWallet, CustomObservableHostname
from stix2 import DomainName  # type: ignore
from stix2 import (
    URL,
    EmailAddress,
    File,
    Identity,
    IPv4Address,
    IPv6Address,
    MarkingDefinition,
    Mutex,
)


def _get_default_custom_properties(
    x_threatlens_score: int,
    created_by: Optional[Identity] = None,
    labels: Optional[List[str]] = None,
) -> Mapping[str, Any]:
    # XXX: Causes an unexpected property (x_threatlens_score) error
    # when creating a Bundle without allow_custom=True flag.
    custom_properties = {X_threatlens_LABELS: labels, X_threatlens_SCORE: x_threatlens_score}

    if created_by is not None:
        custom_properties[X_threatlens_CREATED_BY_REF] = created_by["id"]

    return custom_properties


class ObservableProperties(NamedTuple):
    """Observable properties."""

    value: str
    created_by: Identity
    labels: List[str]
    object_markings: List[MarkingDefinition]
    x_threatlens_score: int


def _get_custom_properties(properties: ObservableProperties) -> Mapping[str, Any]:
    return _get_default_custom_properties(
        created_by=properties.created_by,
        labels=properties.labels,
        x_threatlens_score=properties.x_threatlens_score,
    )


def create_observable_ipv4_address(properties: ObservableProperties) -> IPv4Address:
    """Create an observable representing an IPv4 address."""
    return IPv4Address(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def create_observable_ipv6_address(properties: ObservableProperties) -> IPv6Address:
    """Create an observable representing an IPv6 address."""
    return IPv6Address(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def create_observable_domain_name(properties: ObservableProperties) -> DomainName:
    """Create an observable representing a domain name."""
    return DomainName(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def create_observable_hostname(
    properties: ObservableProperties,
) -> CustomObservableHostname:
    """Create an observable representing a hostname."""
    return CustomObservableHostname(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )  # type: ignore


def create_observable_email_address(properties: ObservableProperties) -> EmailAddress:
    """Create an observable representing an email address."""
    return EmailAddress(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def create_observable_url(properties: ObservableProperties) -> URL:
    """Create an observable representing an URL."""
    return URL(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def _create_observable_file(
    properties: ObservableProperties,
    hashes: Optional[Mapping[str, str]] = None,
    name: Optional[str] = None,
) -> File:
    return File(
        hashes=hashes,
        name=name,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def create_observable_file_md5(properties: ObservableProperties) -> File:
    """Create an observable representing a MD5 hash of a file."""
    return _create_observable_file(
        hashes={"MD5": properties.value}, properties=properties
    )


def create_observable_file_sha1(properties: ObservableProperties) -> File:
    """Create an observable representing a SHA-1 hash of a file."""
    return _create_observable_file(
        hashes={"SHA-1": properties.value}, properties=properties
    )


def create_observable_file_sha256(properties: ObservableProperties) -> File:
    """Create an observable representing a SHA-256 hash of a file."""
    return _create_observable_file(
        hashes={"SHA-256": properties.value}, properties=properties
    )


def create_observable_file_name(properties: ObservableProperties) -> File:
    """Create an observable representing a file name."""
    return _create_observable_file(name=properties.value, properties=properties)


def create_observable_mutex(properties: ObservableProperties) -> Mutex:
    """Create an observable representing a mutex."""
    return Mutex(
        name=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )


def create_observable_cryptocurrency_wallet(
    properties: ObservableProperties,
) -> CustomObservableCryptocurrencyWallet:
    """Create an observable representing a cryptocurrency wallet."""
    return CustomObservableCryptocurrencyWallet(
        value=properties.value,
        object_marking_refs=properties.object_markings,
        custom_properties=_get_custom_properties(properties),
    )  # type: ignore
