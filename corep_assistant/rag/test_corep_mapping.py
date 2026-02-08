from schemas.corep_c01_schema import COREP_C01_SCHEMA
from rag.corep_retriever import retrieve_for_corep_field
from validation.audit_trail import AuditTrail

for field in COREP_C01_SCHEMA:
    texts = retrieve_for_corep_field(field, k=2)

    audit = AuditTrail(
        corep_row=field.row,
        corep_label=field.label,
        justification_texts=texts,
    )

    audit.pretty_print()

