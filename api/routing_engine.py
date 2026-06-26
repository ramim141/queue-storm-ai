from .enums import Severity, Department

class RoutingEngine:

    ROUTES = {
        "wrong_transfer": {
            "department": "dispute_resolution",
            "severity": Severity.HIGH.value,
            "human_review_required": True,
        },

        "payment_failed": {
            "department": "payments_ops",
            "severity": "medium",
            "human_review_required": False,
        },

        "refund_request": {
            "department": "dispute_resolution",
            "severity": "medium",
            "human_review_required": True,
        },

        "duplicate_payment": {
            "department": "payments_ops",
            "severity": "medium",
            "human_review_required": False,
        },

        "merchant_settlement_delay": {
            "department": "merchant_operations",
            "severity": "medium",
            "human_review_required": False,
        },

        "agent_cash_in_issue": {
            "department": "agent_operations",
            "severity": "high",
            "human_review_required": True,
        },

        "phishing_or_social_engineering": {
            "department": "fraud_risk",
            "severity": "critical",
            "human_review_required": True,
        },

        "other": {
            "department": "customer_support",
            "severity": "low",
            "human_review_required": False,
        }
    }

    def get_route(self, case_type):
        return self.ROUTES.get(case_type, self.ROUTES["other"])