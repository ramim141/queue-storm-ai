from .constants import (
    SAFE_CUSTOMER_REPLY,
    DEFAULT_CONFIDENCE,
)

class FallbackResponse:

    @staticmethod
    def get():

        return {

            "agent_summary":
                "Unable to generate AI summary. Manual review recommended.",

            "recommended_next_action":
                "Forward the case to the assigned support department.",

            "customer_reply":
                "We have received your complaint. Our support team will review your case and contact you if additional information is required.",
            
            "confidence": DEFAULT_CONFIDENCE,

            "reason_codes":[
                "fallback_response"
            ]
        }