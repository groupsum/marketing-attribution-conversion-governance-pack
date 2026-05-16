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

- `adr:conversion-attribution-authority` - Conversion Attribution Authority
- `adr:click-id-and-server-conversion-boundary` - Click ID And Server Conversion Boundary

## Included SPECs

- `spc:w3c-attribution-reporting-contract` - W3C Attribution Reporting Contract
- `spc:google-microsoft-click-id-contract` - Google Microsoft Click ID Contract
- `spc:meta-tiktok-linkedin-capi-contract` - Meta TikTok LinkedIn CAPI Contract
- `spc:iab-ecapi-admap-contract` - IAB ECAPI ADMaP Contract

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
