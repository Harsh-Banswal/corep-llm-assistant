from llm.prompts import EXPLAIN_VALIDATION_PROMPT
from llm.llm_client import get_llm

def explain_issue(corep_row, issue, regulatory_texts):
    llm = get_llm()

    prompt = EXPLAIN_VALIDATION_PROMPT.format(
        row=corep_row,
        issue=issue,
        reg_text="\n\n".join(regulatory_texts)
    )

    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception:
        # Fallback explanation if API quota is exceeded
        return (
            "Fallback explanation: Total Own Funds must equal the sum of "
            "Common Equity Tier 1, Additional Tier 1, and Tier 2 capital "
            "as defined in PRA Own Funds rules. Any inconsistency must be "
            "resolved before COREP submission."
        )

