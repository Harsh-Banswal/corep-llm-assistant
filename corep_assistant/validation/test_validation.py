from validation.corep_report import COREP_REPORT
from validation.corep_validator import validate_corep_report

issues = validate_corep_report(COREP_REPORT)

if not issues:
    print("COREP report validation passed ✔")
else:
    print("COREP report validation issues found:")
    for issue in issues:
        print("-", issue)

