# ssot-pack-marketing-attribution-conversion

Installable SSOT governance pack for attribution reporting, click IDs, tracking templates, offline conversions, conversion APIs, ECAPI, and ADMaP.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:marketing-attribution-conversion`
- Priority: `P1.3`
- PyPI package: `ssot-pack-marketing-attribution-conversion`
- Import package: `ssot_pack_marketing_attribution_conversion`
- GitHub repository: `groupsum/marketing-attribution-conversion-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-marketing-attribution-conversion`

## Domain Focus

Marketing Attribution And Conversion Measurement

## Authority Sources

- W3C Attribution Reporting
- IAB Tech Lab ADMaP
- IAB Tech Lab ECAPI
- Google Ads auto-tagging and ValueTrack
- Google Ads click and enhanced conversion uploads
- Microsoft Advertising UET CAPI and offline conversions
- Meta Conversions API
- TikTok Events API
- LinkedIn Conversions API

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
uv add ssot-pack-marketing-attribution-conversion
uv add ssot-registry ssot-pack-marketing-attribution-conversion
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-marketing-attribution-conversion
uvx --from ssot-registry ssot pack sync . ssot-pack-marketing-attribution-conversion
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

- GitHub repository: https://github.com/groupsum/marketing-attribution-conversion-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-marketing-attribution-conversion/
- SSOT Registry: https://pypi.org/project/ssot-registry/
