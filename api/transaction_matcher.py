import re
from datetime import datetime


class TransactionMatcher:

    def extract_amount(self, complaint):
        match = re.search(r"\d+(?:\.\d+)?", complaint)
        if match:
            return float(match.group())
        return None

    def extract_phone(self, complaint):
        match = re.search(r"(01[3-9]\d{8})", complaint)
        if match:
            return match.group()
        return None

    def find_match(self, complaint, transactions):

        amount = self.extract_amount(complaint)
        phone = self.extract_phone(complaint)

        best_match = None
        highest_score = -1

        for txn in transactions:

            score = 0

            # Amount Match (40)
            if amount is not None and txn["amount"] == amount:
                score += 40

            # Phone Match (30)
            if phone:
                counterparty = txn.get("counterparty", "").replace("+88", "")
                if counterparty == phone:
                    score += 30

            # Completed Transaction (15)
            if txn["status"] == "completed":
                score += 15

            # Transfer Type (15)
            if txn["type"] == "transfer":
                score += 15

            if score > highest_score:
                highest_score = score
                best_match = txn

        return best_match