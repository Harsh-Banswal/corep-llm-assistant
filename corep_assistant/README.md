PROJECT TITLE
-------------
LLM-Assisted PRA COREP Regulatory Reporting Assistant (Prototype)


1. PROJECT OVERVIEW
-------------------

This project implements a prototype of an LLM-assisted regulatory
reporting assistant for UK banks subject to the PRA Rulebook.

The focus of the prototype is on COREP Own Funds reporting
(COREP C 01.00), which requires banks to accurately report capital
components such as Common Equity Tier 1 (CET1), Additional Tier 1 (AT1),
Tier 2 capital, and Total Own Funds.

The system demonstrates an end-to-end workflow:
- deterministic validation of COREP data
- retrieval of relevant PRA / CRR regulatory text
- LLM-assisted explanation of validation issues
- audit-friendly and non-hallucinating design


Basically, 
I built an LLM-assisted PRA COREP reporting prototype that validates Own
Funds data using deterministic regulatory rules, retrieves relevant PRA
regulatory text, and uses an LLM only to explain validation issues in
natural language. The system is auditable, non-hallucinating, and
includes a fallback mechanism to handle LLM API quota limitations.


1.2
Install the python libs which are present in requirements.txt file


2. PROJECT OBJECTIVES
--------------------
The main objectives of this prototype are:

- Reduce manual effort in interpreting COREP rules
- Avoid LLM hallucination by grounding explanations in regulation
- Demonstrate how LLMs can assist (not replace) regulatory logic
- Provide traceability between validation rules and PRA text
- Show an end-to-end working flow on a scoped COREP template


3. HIGH-LEVEL ARCHITECTURE
--------------------------
The system follows a layered architecture:

1. COREP Data Layer
   - Structured COREP report values (mocked for demo)

2. Validation Layer (Deterministic)
   - Applies PRA / CRR rules (e.g. Total Own Funds consistency)

3. Retrieval Layer (RAG)
   - Retrieves only relevant regulatory text for affected COREP rows

4. LLM Explanation Layer
   - Generates human-readable explanations for validation issues although it is not giving llm output because openai key issue( not in the logic ) so instead of that a fallback expalnation is written in the file.
   A whole explanation in provided in the "explanation.txt" file 

5. Demo Orchestration Layer
   - Runs the complete workflow end-to-end


4. PROJECT STRUCTURE
--------------------
corep_llm_assistant/
│
├── data/
│   └── pra_own_funds.txt
│      (Extracted PRA / CRR Own Funds rules)
│
├── schemas/
│   └── corep_c01_schema.py
│      (COREP C 01.00 row definitions)
│
├── validation/
│   ├── corep_report.py
│   │   (Mock COREP report data)
│   └── corep_validator.py
│       (Deterministic validation rules)
│
├── rag/
│   ├── corep_retriever.py
│   └── test_corep_mapping.py
│       (Retrieval of relevant regulatory text)
│
├── llm/
│   ├── llm_client.py
│   ├── explainer.py
│   └── prompts.py
│       (LLM integration and explanation logic)
│
├── demo/
│   └── run_assistant.py
│       (End-to-end demo runner)
│
├── output/
│   (Optional outputs / logs)
│
├── env/
│   (Python virtual environment)
│
└── README.txt


5. INPUTS AND OUTPUTS
---------------------

INPUTS:
- COREP report data (CET1, AT1, Tier 2, Total Own Funds)
- PRA / CRR regulatory text (Own Funds Part)
- COREP schema definitions
- Implicit natural-language explanation request

OUTPUTS:
- Validation success message (if data is compliant)
OR
- Validation issue description
- Regulatory-grounded explanation of the issue
- Traceability to PRA Own Funds rules


6. VALIDATION LOGIC (EXAMPLE)
-----------------------------
Implemented validation rule:

Total Own Funds (R040)
= CET1 (R010) + AT1 (R020) + Tier 2 (R030)

If this condition is violated, the system raises a validation issue.
The LLM is then used only to explain the issue.


7. LLM USAGE PHILOSOPHY
----------------------
The LLM is NOT used for:
- Regulatory interpretation
- Validation logic
- Decision making

The LLM IS used for:
- Explaining detected issues in human-readable language
- Improving analyst usability
- Summarising regulatory justification

This ensures:
- No hallucination
- Deterministic correctness
- Regulatory auditability


8. HOW TO RUN THE PROJECT
-------------------------

1. Activate the virtual environment:
   source env/bin/activate

2. (Optional) Set OpenAI API key:
   export OPENAI_API_KEY="your_key_here"
   or
   put it in .env file presented in the folder without qoutes 
	the same syntax should be used (OPENAI_API_KEY=YOUR API KEY).

3. Run the demo:
   python3 -m demo.run_assistant

EXPECTED BEHAVIOUR:
- If COREP data is inconsistent → validation issue + explanation
- If COREP data is correct → successful validation message


9. DEMO SCENARIOS
-----------------
The project supports two demo scenarios via a toggle in
validation/corep_report.py:

- Non-compliant COREP data (shows validation + explanation)
- Compliant COREP data (shows successful validation)


10. LIMITATIONS
---------------
- Prototype supports a limited subset of COREP (Own Funds only)
- Regulatory text is pre-extracted (not live web retrieval)
- LLM explanation may fall back to deterministic text if API quota is unavailable


11. CONCLUSION
--------------
This prototype demonstrates how LLMs can safely assist regulatory
reporting by explaining deterministic validation outcomes while
maintaining correctness, traceability, and auditability.

