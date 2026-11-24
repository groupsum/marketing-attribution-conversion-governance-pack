# Marketing Attribution And Conversion Measurement pack guide

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
- GitHub repository: [groupsum/marketing-attribution-conversion-governance-pack](https://github.com/groupsum/marketing-attribution-conversion-governance-pack)
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

- [`adr:browser-attribution-reporting-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1001-browser-attribution-reporting-policy.yaml) - Browser Attribution Reporting Policy
- [`adr:click-id-capture-and-retention-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1002-click-id-capture-and-retention-policy.yaml) - Click ID Capture And Retention Policy
- [`adr:tracking-template-parameter-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1003-tracking-template-parameter-policy.yaml) - Tracking Template Parameter Policy
- [`adr:offline-conversion-upload-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1004-offline-conversion-upload-policy.yaml) - Offline Conversion Upload Policy
- [`adr:enhanced-conversion-identifier-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1005-enhanced-conversion-identifier-policy.yaml) - Enhanced Conversion Identifier Policy
- [`adr:server-conversion-api-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1006-server-conversion-api-policy.yaml) - Server Conversion API Policy
- [`adr:conversion-consent-and-privacy-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1007-conversion-consent-and-privacy-policy.yaml) - Conversion Consent And Privacy Policy
- [`adr:clean-room-attribution-protocol-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1008-clean-room-attribution-protocol-policy.yaml) - Clean Room Attribution Protocol Policy
- [`adr:industry-conversion-event-protocol-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1009-industry-conversion-event-protocol-policy.yaml) - Industry Conversion Event Protocol Policy
- [`adr:click-measurement-quality-policy`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/adr/ADR-1010-click-measurement-quality-policy.yaml) - Click Measurement Quality Policy

## Included SPECs

- [`spc:w3c-attribution-reporting-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2001-w3c-attribution-reporting-requirements.yaml) - W3C Attribution Reporting Requirements
- [`spc:google-ads-auto-tagging-click-id-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2002-google-ads-auto-tagging-click-id-requirements.yaml) - Google Ads Auto-Tagging Click ID Requirements
- [`spc:google-ads-valuetrack-parameter-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2003-google-ads-valuetrack-parameter-requirements.yaml) - Google Ads ValueTrack Parameter Requirements
- [`spc:google-ads-click-conversion-upload-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2004-google-ads-click-conversion-upload-requirements.yaml) - Google Ads Click Conversion Upload Requirements
- [`spc:google-ads-enhanced-conversion-lead-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2005-google-ads-enhanced-conversion-lead-requirements.yaml) - Google Ads Enhanced Conversion Lead Requirements
- [`spc:microsoft-uet-capi-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2006-microsoft-uet-capi-requirements.yaml) - Microsoft UET CAPI Requirements
- [`spc:microsoft-offline-conversion-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2007-microsoft-offline-conversion-requirements.yaml) - Microsoft Offline Conversion Requirements
- [`spc:microsoft-url-tracking-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2008-microsoft-url-tracking-requirements.yaml) - Microsoft URL Tracking Requirements
- [`spc:meta-conversions-api-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2009-meta-conversions-api-requirements.yaml) - Meta Conversions API Requirements
- [`spc:meta-pixel-conversion-event-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2010-meta-pixel-conversion-event-requirements.yaml) - Meta Pixel Conversion Event Requirements
- [`spc:tiktok-events-api-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2011-tiktok-events-api-requirements.yaml) - TikTok Events API Requirements
- [`spc:linkedin-conversions-api-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2012-linkedin-conversions-api-requirements.yaml) - LinkedIn Conversions API Requirements
- [`spc:linkedin-conversion-source-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2013-linkedin-conversion-source-requirements.yaml) - LinkedIn Conversion Source Requirements
- [`spc:iab-ecapi-conversion-event-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2014-iab-ecapi-conversion-event-requirements.yaml) - IAB ECAPI Conversion Event Requirements
- [`spc:iab-admap-clean-room-attribution-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2015-iab-admap-clean-room-attribution-requirements.yaml) - IAB ADMaP Clean Room Attribution Requirements
- [`spc:iab-click-measurement-quality-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2016-iab-click-measurement-quality-requirements.yaml) - IAB Click Measurement Quality Requirements
- [`spc:iab-video-ad-measurement-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2017-iab-video-ad-measurement-requirements.yaml) - IAB Video Ad Measurement Requirements
- [`spc:mrc-measurement-quality-reference-requirements`](https://github.com/groupsum/marketing-attribution-conversion-governance-pack/blob/master/src/ssot_pack_marketing_attribution_conversion/templates/specs/SPEC-2018-mrc-measurement-quality-reference-requirements.yaml) - MRC Measurement Quality Reference Requirements

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

## Normative ownership boundary

Removed duplicate ad measurement ownership and added an attribution-input profile.
