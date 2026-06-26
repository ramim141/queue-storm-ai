import re
from .constants import SAFE_CUSTOMER_REPLY

class SafetyEngine:

    FORBIDDEN_WORDS = [
        "pin",
        "otp",
        "password",
        "cvv",
        "card number",
        "full card number"
    ]

    FORBIDDEN_PROMISES = [
        "we will refund",
        "refund will be processed",
        "money will be returned",
        "we guarantee",
        "we recovered",
        "account unblocked"
    ]

    SAFE_REPLY = (
        "We have received your concern. Our support team will review the "
        "available information. If additional details are required, we will "
        "contact you through official support channels."
    )

    def sanitize(self, response):

        reply = response.get("customer_reply", "").lower()

        # PIN / OTP / Password check
        for word in self.FORBIDDEN_WORDS:
            if word in reply:
                response["customer_reply"] = SAFE_CUSTOMER_REPLY
                break

        # Unauthorized promises
        reply = response["customer_reply"].lower()

        for phrase in self.FORBIDDEN_PROMISES:
            if phrase in reply:
                response["customer_reply"] = SAFE_CUSTOMER_REPLY
                break

        return response