"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_marketing_attribution_conversion import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:w3c-attribution-reporting-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-w3c-attribution-reporting-requirements.yaml"
