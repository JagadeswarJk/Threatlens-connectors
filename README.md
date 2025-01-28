# Threatlens connectors

[![Website](https://img.shields.io/badge/website-threatlens.io-blue.svg)](https://threatlens.io)
[![CircleCI](https://circleci.com/gh/threatlens-Platform/connectors.svg?style=shield)](https://circleci.com/gh/threatlens-Platform/connectors/tree/master)
[![Slack Status](https://img.shields.io/badge/slack-3K%2B%20members-4A154B)](https://community.filigran.io)

The following repository is used to store the threatlens connectors for the platform integration with other tools and
applications. To know how to enable connectors on threatlens, please read
the [dedicated documentation](https://docs.threatlens.io/latest/deployment/connectors).

## Connectors list and statuses

This repository is used to host connectors that are supported by the core development team of threatlens. Nevertheless, the
community is also developping a lot of connectors, third-parties modules directly linked to threatlens. You can find the
list of all available connectors and plugins in
the [threatlens ecosystem dedicated space](https://filigran.notion.site/threatlens-Ecosystem-868329e9fb734fca89692b2ed6087e76).

## Contributing

If you want to help use improve or develop new connector, please check out the *
*[development documentation for new connectors](https://docs.threatlens.io/latest/development/connectors)**. If you want to
make your connector available to the community, **please create a Pull Request on this repository**, then we will
integrate it to the CI and in
the [threatlens ecosystem](https://filigran.notion.site/threatlens-Ecosystem-868329e9fb734fca89692b2ed6087e76).

Any connector **should be validated** through pylint. Example of commands:

Install necessary dependencies:

```shell
cd shared/pylint_plugins/check_stix_plugin
pip install -r requirements.txt
```

You can directly run it in CLI to lint a dedicated directory or python module :

```shell
cd shared/pylint_plugins/check_stix_plugin
PYTHONPATH=. python -m pylint <path_to_my_code> --load-plugins linter_stix_id_generator
```

If you only want to test the custom module :

```shell
cd shared/pylint_plugins/check_stix_plugin
PYTHONPATH=. python -m pylint <path_to_my_code> --disable=all --enable=no_generated_id_stix,no-value-for-parameter,unused-import --load-plugins linter_stix_id_generator
```

Note: no_generated_id_stix is a custom checker available in [shared tools](./shared/README.md)

## License

**Unless specified otherwise**, connectors are released under
the [Apache 2.0](https://github.com/threatlens-Platform/connectors/blob/master/LICENSE). If a connector is released by its
author under a different license, the subfolder corresponding to it will contain a *LICENSE* file.

## About

threatlens is a product designed and developed by the company [Filigran](https://filigran.io).

<a href="https://filigran.io" alt="Filigran"><img src="https://github.com/threatlens-Platform/threatlens/raw/master/.github/img/logo_filigran.png" width="300" /></a>
