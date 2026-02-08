from dataclasses import dataclass
from typing import List

@dataclass
class AuditTrail:
    corep_row: str
    corep_label: str
    justification_texts: List[str]

    def pretty_print(self):
        print(f"\nCOREP Row {self.corep_row}: {self.corep_label}")
        print("Justified by the following regulatory text:")
        for i, text in enumerate(self.justification_texts, 1):
            print(f"\n[{i}] {text}")

