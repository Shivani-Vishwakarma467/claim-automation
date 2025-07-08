# claim_processor.py

import random

class Claim:
    def __init__(self, claim_id, document_text):
        self.claim_id = claim_id
        self.document_text = document_text
        self.complexity_score = 0
        self.is_simple = None

class ClaimProcessor:
    def __init__(self):
        pass

    def extract_info(self, document_text):
        # Simulate extraction
        extracted_info = {
            "has_all_fields": "patient" in document_text and "amount" in document_text,
            "length": len(document_text)
        }
        return extracted_info

    def assess_complexity(self, extracted_info):
        # Simple complexity assessment
        if not extracted_info["has_all_fields"]:
            return 8  # High complexity
        elif extracted_info["length"] < 50:
            return 2  # Simple
        else:
            return 5  # Medium

    def classify_claim(self, claim):
        extracted_info = self.extract_info(claim.document_text)
        claim.complexity_score = self.assess_complexity(extracted_info)
        claim.is_simple = claim.complexity_score <= 3
        return claim

    def route_claim(self, claim):
        if claim.is_simple:
            return "Auto-processed ✅"
        else:
            return f"Flagged for manual review 🧑‍⚖️ | Score: {claim.complexity_score}"

# Sample execution
if __name__ == "__main__":
    claims = [
        Claim("001", "patient: John Doe, amount: 1000, procedure: MRI"),
        Claim("002", "procedure: surgery only"),
        Claim("003", "patient: Alice, amount: 2000")
    ]

    processor = ClaimProcessor()
    for c in claims:
        c = processor.classify_claim(c)
        print(f"Claim ID: {c.claim_id} → {processor.route_claim(c)}")

