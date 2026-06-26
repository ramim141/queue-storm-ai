from enum import Enum


class CaseType(str, Enum):
    WRONG_TRANSFER = "wrong_transfer"
    PAYMENT_FAILED = "payment_failed"
    REFUND_REQUEST = "refund_request"
    DUPLICATE_PAYMENT = "duplicate_payment"
    MERCHANT_SETTLEMENT_DELAY = "merchant_settlement_delay"
    AGENT_CASH_IN_ISSUE = "agent_cash_in_issue"
    PHISHING = "phishing_or_social_engineering"
    OTHER = "other"


class EvidenceVerdict(str, Enum):
    CONSISTENT = "consistent"
    INCONSISTENT = "inconsistent"
    INSUFFICIENT_DATA = "insufficient_data"


class Severity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Department(str, Enum):
    CUSTOMER_SUPPORT = "customer_support"
    DISPUTE = "dispute_resolution"
    PAYMENTS = "payments_ops"
    FRAUD = "fraud_risk"
    AGENT = "agent_operations"
    MERCHANT = "merchant_operations"