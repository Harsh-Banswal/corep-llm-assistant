from validation.corep_report import COREP_REPORT
from validation.corep_validator import validate_corep_report
from schemas.corep_c01_schema import COREP_C01_SCHEMA
from rag.corep_retriever import retrieve_for_corep_field
from llm.explainer import explain_issue

issues = validate_corep_report(COREP_REPORT)

if not issues:
    print("COREP report validated successfully ✔")
else:
    for issue in issues:
        print("\nValidation issue detected:")
        print(issue)

        # For demo purposes, assume issue relates to Total Own Funds
        field = next(f for f in COREP_C01_SCHEMA if f.row == "R040")
        reg_texts = retrieve_for_corep_field(field)

        explanation = explain_issue(
            corep_row=field.row,
            issue=issue,
            regulatory_texts=reg_texts
        )

        print("\nLLM Explanation:")
        print(explanation)

