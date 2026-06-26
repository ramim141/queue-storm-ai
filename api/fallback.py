from .constants import SAFE_CUSTOMER_REPLY, DEFAULT_CONFIDENCE


def get_fallback_response(case_type="other"):
    return {
        "agent_summary": (
            f"Automatic fallback response for {case_type}."
        ),
        "recommended_next_action": (
            "Please review this case manually."
        ),
        "customer_reply": SAFE_CUSTOMER_REPLY,
        "confidence": DEFAULT_CONFIDENCE,
        "reason_codes": [
            "LLM_UNAVAILABLE"
        ]
    }