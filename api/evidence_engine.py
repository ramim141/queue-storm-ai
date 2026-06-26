
from .enums import EvidenceVerdict

class EvidenceEngine:

    def evaluate(self, complaint, matched_transaction):

        # কোনো transaction match না হলে
        if matched_transaction is None:
            return {
                "verdict": "insufficient_data",
                "reason_codes": [
                    "transaction_not_found"
                ]
            }

        status = matched_transaction.get("status", "").lower()

        # সফল transaction
        if status == "completed":
            return {
                "verdict": EvidenceVerdict.CONSISTENT.value,
                "reason_codes": [
                    "transaction_match",
                    "completed_transaction"
                ]
            }

        # Failed
        if status == "failed":
            return {
                "verdict": "inconsistent",
                "reason_codes": [
                    "transaction_failed"
                ]
            }

        # Pending
        if status == "pending":
            return {
                "verdict": "insufficient_data",
                "reason_codes": [
                    "transaction_pending"
                ]
            }

        # Reversed
        if status == "reversed":
            return {
                "verdict": "inconsistent",
                "reason_codes": [
                    "transaction_reversed"
                ]
            }

        return {
            "verdict": "insufficient_data",
            "reason_codes": [
                "unknown_status"
            ]
        }