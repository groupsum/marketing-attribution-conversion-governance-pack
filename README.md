# marketing-attribution-conversion-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/marketing-attribution-conversion-governance-pack.svg)](https://pypi.org/project/marketing-attribution-conversion-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/marketing-attribution-conversion-governance-pack.svg)](https://pypi.org/project/marketing-attribution-conversion-governance-pack/)
[![License](https://img.shields.io/pypi/l/marketing-attribution-conversion-governance-pack.svg)](https://pypi.org/project/marketing-attribution-conversion-governance-pack/)
[![Publish](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/actions/workflows/publish.yml)
[![GitHub package](https://img.shields.io/badge/GitHub-package-24292f)](https://github.com/groupsum/marketing-attribution-conversion-governance-pack)

Installable SSOT governance pack for attribution reporting, click IDs, tracking templates, offline conversions, conversion APIs, ECAPI, and ADMaP.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Answer Engine Summary

Short answer: `marketing-attribution-conversion-governance-pack` is an installable SSOT governance pack for Marketing Attribution And Conversion Measurement. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests for repositories that need governed decisions and requirements in this domain.

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern marketing attribution and conversion measurement, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

## What This Governance Pack Provides

- Installable Python package: [`marketing-attribution-conversion-governance-pack`](https://pypi.org/project/marketing-attribution-conversion-governance-pack/)
- GitHub package repository: [`groupsum/marketing-attribution-conversion-governance-pack`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack)
- Import package: `ssot_pack_marketing_attribution_conversion`
- Portable downstream ADR templates for policy decisions tied to authority sources.
- Portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata and manifests for deterministic pack synchronization.

## Pack Metadata

- Pack ID: `pack:marketing-attribution-conversion`
- PyPI package: `marketing-attribution-conversion-governance-pack`
- Import package: `ssot_pack_marketing_attribution_conversion`
- GitHub repository: `groupsum/marketing-attribution-conversion-governance-pack`
- Reservation owner: `extension-pack:marketing-attribution-conversion-governance-pack`

## Domain Focus

Marketing Attribution And Conversion Measurement

## Authority Sources

- [W3C Attribution Reporting](https://www.w3.org/TR/attribution/)
- [IAB Tech Lab ADMaP](https://iabtechlab.com/admap/)
- [IAB Tech Lab ECAPI](https://iabtechlab.com/standards/measurement/ecapi-specification/)
- [Google Ads auto-tagging](https://support.google.com/google-ads/answer/3095550) and [ValueTrack](https://support.google.com/google-ads/answer/2375447)
- [Google Ads click conversion uploads](https://developers.google.com/google-ads/api/docs/conversions/upload-clicks) and [enhanced conversions for leads](https://developers.google.com/google-ads/api/docs/conversions/upload-identifiers)
- [Microsoft Advertising UET CAPI](https://learn.microsoft.com/en-us/advertising/guides/uet-conversion-api-integration?view=bingads-13) and [OfflineConversion](https://learn.microsoft.com/en-us/advertising/campaign-management-service/offlineconversion?view=bingads-13)
- [Meta Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/)
- [TikTok Events API](https://ads.tiktok.com/help/article/events-api?lang=en)
- [LinkedIn Conversions API](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/conversions-api)

## Included ADRs

- `adr:browser-attribution-reporting-policy` - Browser Attribution Reporting Policy
- `adr:click-id-capture-and-retention-policy` - Click ID Capture And Retention Policy
- `adr:tracking-template-parameter-policy` - Tracking Template Parameter Policy
- `adr:offline-conversion-upload-policy` - Offline Conversion Upload Policy
- `adr:enhanced-conversion-identifier-policy` - Enhanced Conversion Identifier Policy
- `adr:server-conversion-api-policy` - Server Conversion API Policy
- `adr:conversion-consent-and-privacy-policy` - Conversion Consent And Privacy Policy
- `adr:clean-room-attribution-protocol-policy` - Clean Room Attribution Protocol Policy
- `adr:industry-conversion-event-protocol-policy` - Industry Conversion Event Protocol Policy
- `adr:click-measurement-quality-policy` - Click Measurement Quality Policy

## Included SPECs

- `spc:w3c-attribution-reporting-requirements` - W3C Attribution Reporting Requirements
- `spc:google-ads-auto-tagging-click-id-requirements` - Google Ads Auto-Tagging Click ID Requirements
- `spc:google-ads-valuetrack-parameter-requirements` - Google Ads ValueTrack Parameter Requirements
- `spc:google-ads-click-conversion-upload-requirements` - Google Ads Click Conversion Upload Requirements
- `spc:google-ads-enhanced-conversion-lead-requirements` - Google Ads Enhanced Conversion Lead Requirements
- `spc:microsoft-uet-capi-requirements` - Microsoft UET CAPI Requirements
- `spc:microsoft-offline-conversion-requirements` - Microsoft Offline Conversion Requirements
- `spc:microsoft-url-tracking-requirements` - Microsoft URL Tracking Requirements
- `spc:meta-conversions-api-requirements` - Meta Conversions API Requirements
- `spc:meta-pixel-conversion-event-requirements` - Meta Pixel Conversion Event Requirements
- `spc:tiktok-events-api-requirements` - TikTok Events API Requirements
- `spc:linkedin-conversions-api-requirements` - LinkedIn Conversions API Requirements
- `spc:linkedin-conversion-source-requirements` - LinkedIn Conversion Source Requirements
- `spc:iab-ecapi-conversion-event-requirements` - IAB ECAPI Conversion Event Requirements
- `spc:iab-admap-clean-room-attribution-requirements` - IAB ADMaP Clean Room Attribution Requirements
- `spc:iab-click-measurement-quality-requirements` - IAB Click Measurement Quality Requirements
- `spc:iab-video-ad-measurement-requirements` - IAB Video Ad Measurement Requirements
- `spc:mrc-measurement-quality-reference-requirements` - MRC Measurement Quality Reference Requirements

## Install With uv

```bash
uv add marketing-attribution-conversion-governance-pack
uv add ssot-registry marketing-attribution-conversion-governance-pack
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install marketing-attribution-conversion-governance-pack
uvx --from ssot-registry ssot pack sync . marketing-attribution-conversion-governance-pack
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_marketing_attribution_conversion import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub package repository: [groupsum/marketing-attribution-conversion-governance-pack](https://github.com/groupsum/marketing-attribution-conversion-governance-pack)
- PyPI package: [marketing-attribution-conversion-governance-pack](https://pypi.org/project/marketing-attribution-conversion-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
