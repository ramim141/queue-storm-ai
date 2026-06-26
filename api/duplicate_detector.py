from datetime import timedelta
from .constants import DUPLICATE_PAYMENT_WINDOW_MINUTES

class DuplicatePaymentDetector:

    def detect(self, transactions):

        if len(transactions) < 2:
            return None

        transactions = sorted(
            transactions,
            key=lambda x: x["timestamp"]
        )

        for i in range(len(transactions) - 1):

            current = transactions[i]
            nxt = transactions[i + 1]

            same_amount = current["amount"] == nxt["amount"]
            same_counterparty = (
                current["counterparty"] == nxt["counterparty"]
            )
            same_type = (
                current["type"] == "payment"
                and nxt["type"] == "payment"
            )

            time_difference = abs(
                nxt["timestamp"] - current["timestamp"]
            )

            if (
                same_amount
                and same_counterparty
                and same_type
                and time_difference <= timedelta(minutes=DUPLICATE_PAYMENT_WINDOW_MINUTES)
            ):
                return {
                    "duplicate": True,
                    "transaction_id": nxt["transaction_id"]
                }

        return None