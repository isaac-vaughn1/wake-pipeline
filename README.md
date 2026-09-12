# wake

A batch data pipeline for AIS vessel-tracking data. Ingests NOAA's nationwide
broadcast archive, reconstructs voyages from raw position reports, and surfaces
coverage anomalies.

> **Status:** in development.

## What this is

Commercial vessels are required to broadcast their position over AIS, an
unencrypted VHF system built for collision avoidance. The US Coast Guard
receives these broadcasts through a network of shore stations, and NOAA
publishes the resulting archive as public-domain data going back to 2009.

Each record is one vessel, at one minute, at one position:

```
MMSI       BaseDateTime          LAT      LON       SOG   COG    VesselName
367123450  2024-01-15T14:23:00Z  29.7142  -95.0331  11.2  183.4  HOUSTON EXPRESS
367123450  2024-01-15T14:24:00Z  29.7108  -95.0329  11.1  184.1  HOUSTON EXPRESS
```

## Dark gaps

The first analytic is **dark gap detection,** finding periods where a vessel
that was broadcasting normally goes silent, then reappears somewhere else.

Detection has to be relative rather than absolute. A gap is only interesting
when other vessels in the same area kept broadcasting through it.

## Data source

Nationwide Automatic Identification System broadcast data, published by the
NOAA Office for Coastal Management via the Marine Cadastre project, sourced
from the U.S. Coast Guard Navigation Center. Licensed CC0 1.0 Universal.

<https://github.com/ocm-marinecadastre/ais-vessel-traffic>

## Licence

MIT
