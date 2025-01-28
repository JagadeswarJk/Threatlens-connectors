# Threatlens abuseipdb ipblacklist

The connector uses the AbuseIPDB API to collect IPlist above a specified risk score.
If you're using a free API key, you must use the 10K limitation in the parameters.

## Installation

### Requirements

- Threatlens Platform >= 6.4.9

### Configuration

| Parameter                            | Docker envvar                | Mandatory    | Description                                                                                                                                                |
| ------------------------------------ |------------------------------| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Threatlens_url`                        | `Threatlens_URL`                | Yes          | The URL of the Threatlens platform.                                                                                                                           |
| `Threatlens_token`                      | `Threatlens_TOKEN`              | Yes          | The default admin token configured in the Threatlens platform parameters file.                                                                                |
| `connector_id`                       | `CONNECTOR_ID`               | Yes          | A valid arbitrary `UUIDv4` that must be unique for this connector.                                                                                         |
| `connector_name`                     | `CONNECTOR_NAME`             | Yes          |                                                                                                                                           |
| `connector_scope`                    | `CONNECTOR_SCOPE`            | Yes          |                                                                                                 |
| `connector_log_level`                | `CONNECTOR_LOG_LEVEL`        | Yes          | The log level for this connector, could be `debug`, `info`, `warn` or `error` (less verbose).                                                              |
| `ABUSEIPDB_URL`                      | `ABUSEIPDB_URL`              | Yes          | the abuse IPDB URL                                                                                                                |
| `ABUSEIPDB_API_KEY`                  | `ABUSEIPDB_API_KEY`          | Yes          | Your Abuse IPDB API KEY                                                                                                                |
| `ABUSEIPDB_SCORE`                    | `ABUSEIPDB_SCORE_FILTER`     | Yes          | AbuseIPDB Score Limitation                                                                                                                |
| `ABUSEIPDB_LIMIT`                    | `ABUSEIPDB_LIMIT`            | Yes          | limit number of result itself                                                                                                               |
| `ABUSEIPDB_INTERVAL`                 | `ABUSEIPDB_LIMIT`            | Yes          | interval between 2 collect itself                                                                                                                |

### Debugging ###

<!-- Any additional information to help future users debug and report detailed issues concerning this connector -->

### Additional information

<!--
Any additional information about this connector
* What information is ingested/updated/changed
* What should the user take into account when using this connector
* ...
-->

