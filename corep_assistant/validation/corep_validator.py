from typing import Dict, List

def validate_corep_report(report: Dict[str, float]) -> List[str]:
    """
    Validate COREP C 01.00 report data
    """
    issues = []

    # Rule 1: Missing rows
    required_rows = ["R010", "R020", "R030", "R040"]
    for row in required_rows:
        if row not in report:
            issues.append(f"Missing value for COREP row {row}")

    # Rule 2: Total Own Funds consistency
    if all(r in report for r in required_rows):
        calculated_total = report["R010"] + report["R020"] + report["R030"]
        reported_total = report["R040"]

        if abs(calculated_total - reported_total) > 1e-6:
            issues.append(
                f"Inconsistent Total Own Funds: "
                f"R040={reported_total}, "
                f"but R010+R020+R030={calculated_total}"
            )

    return issues

