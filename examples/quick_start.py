"""Inspect the installed pack identity."""

from ssot_pack_marketing_attribution_conversion import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:marketing-attribution-conversion"
print(metadata["origin"]["id"])
