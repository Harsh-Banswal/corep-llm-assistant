from dataclasses import dataclass
from typing import List

@dataclass
class CorepField:
    row: str
    label: str
    description: str
    regulatory_concepts: List[str]

COREP_C01_SCHEMA = [
    CorepField(
        row="R010",
        label="Common Equity Tier 1 (CET1)",
        description="Highest quality capital of the institution",
        regulatory_concepts=[
            "Common Equity Tier 1",
            "CET1",
            "Article 26",
            "retained earnings"
        ],
    ),
    CorepField(
        row="R020",
        label="Additional Tier 1 (AT1)",
        description="Additional Tier 1 capital instruments",
        regulatory_concepts=[
            "Additional Tier 1",
            "AT1",
            "Article 51",
            "Article 52"
        ],
    ),
    CorepField(
        row="R030",
        label="Tier 2",
        description="Tier 2 capital instruments",
        regulatory_concepts=[
            "Tier 2",
            "Article 62",
            "Article 63"
        ],
    ),
    CorepField(
        row="R040",
        label="Total Own Funds",
        description="Sum of CET1, AT1 and Tier 2",
        regulatory_concepts=[
            "Total Own Funds",
            "Tier 1 capital",
            "Tier 2 capital"
        ],
    ),
]

