# marketing-attribution-conversion-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>marketing-attribution-conversion-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for attribution reporting, click IDs, tracking templates, offline conversions, conversion APIs, ECAPI, and ADMaP.</p>
<p align="center">
<a href="https://pypi.org/project/marketing-attribution-conversion-governance-pack/"><img alt="pypi: marketing-attribution-conversion-governance-pack" src="https://img.shields.io/pypi/v/marketing-attribution-conversion-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev2" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev2&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/marketing-attribution-conversion-governance-pack/"><img alt="Monthly PyPI downloads: marketing-attribution-conversion-governance-pack" src="https://img.shields.io/pypi/dm/marketing-attribution-conversion-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/README.md"><img alt="README hits: marketing-attribution-conversion-governance-pack" src="https://hits.sh/github.com/groupsum/marketing-attribution-conversion-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for attribution reporting, click IDs, tracking templates, offline conversions, conversion APIs, ECAPI, and ADMaP.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern marketing attribution and conversion measurement, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Marketing Attribution And Conversion Measurement.

### Features

**Included ADRs**

- [`adr:browser-attribution-reporting-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1001-browser-attribution-reporting-policy.yaml) — Browser Attribution Reporting Policy
- [`adr:click-id-capture-and-retention-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1002-click-id-capture-and-retention-policy.yaml) — Click ID Capture And Retention Policy
- [`adr:tracking-template-parameter-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1003-tracking-template-parameter-policy.yaml) — Tracking Template Parameter Policy
- [`adr:offline-conversion-upload-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1004-offline-conversion-upload-policy.yaml) — Offline Conversion Upload Policy
- [`adr:enhanced-conversion-identifier-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1005-enhanced-conversion-identifier-policy.yaml) — Enhanced Conversion Identifier Policy
- [`adr:server-conversion-api-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1006-server-conversion-api-policy.yaml) — Server Conversion API Policy
- [`adr:conversion-consent-and-privacy-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1007-conversion-consent-and-privacy-policy.yaml) — Conversion Consent And Privacy Policy
- [`adr:clean-room-attribution-protocol-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1008-clean-room-attribution-protocol-policy.yaml) — Clean Room Attribution Protocol Policy
- [`adr:industry-conversion-event-protocol-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1009-industry-conversion-event-protocol-policy.yaml) — Industry Conversion Event Protocol Policy
- [`adr:attribution-consumes-canonical-ad-measurement-results`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1011-attribution-consumes-canonical-ad-measurement-results.yaml) — Attribution Consumes Canonical Ad Measurement Results

**Included SPECs**

- [`spc:w3c-attribution-reporting-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2001-w3c-attribution-reporting-requirements.yaml) — W3C Attribution Reporting Requirements
- [`spc:google-ads-auto-tagging-click-id-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2002-google-ads-auto-tagging-click-id-requirements.yaml) — Google Ads Auto-Tagging Click ID Requirements
- [`spc:google-ads-valuetrack-parameter-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2003-google-ads-valuetrack-parameter-requirements.yaml) — Google Ads ValueTrack Parameter Requirements
- [`spc:google-ads-click-conversion-upload-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2004-google-ads-click-conversion-upload-requirements.yaml) — Google Ads Click Conversion Upload Requirements
- [`spc:google-ads-enhanced-conversion-lead-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2005-google-ads-enhanced-conversion-lead-requirements.yaml) — Google Ads Enhanced Conversion Lead Requirements
- [`spc:microsoft-uet-capi-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2006-microsoft-uet-capi-requirements.yaml) — Microsoft UET CAPI Requirements
- [`spc:microsoft-offline-conversion-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2007-microsoft-offline-conversion-requirements.yaml) — Microsoft Offline Conversion Requirements
- [`spc:microsoft-url-tracking-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2008-microsoft-url-tracking-requirements.yaml) — Microsoft URL Tracking Requirements
- [`spc:meta-conversions-api-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2009-meta-conversions-api-requirements.yaml) — Meta Conversions API Requirements
- [`spc:meta-pixel-conversion-event-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2010-meta-pixel-conversion-event-requirements.yaml) — Meta Pixel Conversion Event Requirements
- [`spc:tiktok-events-api-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2011-tiktok-events-api-requirements.yaml) — TikTok Events API Requirements
- [`spc:linkedin-conversions-api-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2012-linkedin-conversions-api-requirements.yaml) — LinkedIn Conversions API Requirements
- [`spc:linkedin-conversion-source-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2013-linkedin-conversion-source-requirements.yaml) — LinkedIn Conversion Source Requirements
- [`spc:iab-ecapi-conversion-event-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2014-iab-ecapi-conversion-event-requirements.yaml) — IAB ECAPI Conversion Event Requirements
- [`spc:iab-admap-clean-room-attribution-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2015-iab-admap-clean-room-attribution-requirements.yaml) — IAB ADMaP Clean Room Attribution Requirements
- [`spc:ad-measurement-to-attribution-input-profile`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2019-ad-measurement-to-attribution-input-profile.yaml) — Ad Measurement To Attribution Input Profile

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add marketing-attribution-conversion-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install marketing-attribution-conversion-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add marketing-attribution-conversion-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_marketing_attribution_conversion import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:marketing-attribution-conversion"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:marketing-attribution-conversion` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/examples/usage.py).

```python
"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_marketing_attribution_conversion import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:w3c-attribution-reporting-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-w3c-attribution-reporting-requirements.yaml"
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `marketing-attribution-conversion-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_marketing_attribution_conversion
uv run ssot pack preflight . ssot_pack_marketing_attribution_conversion --all
uv run ssot pack sync . ssot_pack_marketing_attribution_conversion --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_marketing_attribution_conversion` in SSOT Registry. Review reservation owner `extension-pack:marketing-attribution-conversion-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Removed duplicate ad measurement ownership and added an attribution-input profile.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_marketing_attribution_conversion` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/marketing-attribution-conversion-governance-pack)
- [Issues](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/issues)
- [Repository](https://github.com/groupsum/marketing-attribution-conversion-governance-pack)
- [pypi: marketing-attribution-conversion-governance-pack](https://pypi.org/project/marketing-attribution-conversion-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:marketing-attribution-conversion`. The pack's reservation owner is `extension-pack:marketing-attribution-conversion-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [W3C Attribution Reporting](https://www.w3.org/TR/attribution/)
- [IAB Tech Lab ADMaP](https://iabtechlab.com/admap/)
- [IAB Tech Lab ECAPI](https://iabtechlab.com/standards/measurement/ecapi-specification/)
- [Google Ads auto-tagging](https://support.google.com/google-ads/answer/3095550) and [ValueTrack](https://support.google.com/google-ads/answer/2375447)
- [Google Ads click conversion uploads](https://developers.google.com/google-ads/api/docs/conversions/upload-clicks) and [enhanced conversions for leads](https://developers.google.com/google-ads/api/docs/conversions/upload-identifiers)
- [Microsoft Advertising UET CAPI](https://learn.microsoft.com/en-us/advertising/guides/uet-conversion-api-integration?view=bingads-13) and [OfflineConversion](https://learn.microsoft.com/en-us/advertising/campaign-management-service/offlineconversion?view=bingads-13)
- [Meta Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/)
- [TikTok Events API](https://ads.tiktok.com/help/article/events-api?lang=en)
- [LinkedIn Conversions API](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/conversions-api)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
