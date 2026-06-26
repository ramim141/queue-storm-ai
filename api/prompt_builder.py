import json


class PromptBuilder:

    def build(
        self,
        complaint,
        transaction_history,
        case_type,
        evidence_verdict,
        department,
        severity,
    ):

        return f"""
You are an AI fintech support investigator.

Analyze the following support ticket.

Customer Complaint:
{complaint}

Transaction History:
{json.dumps(
    transaction_history,
    indent=2,
    default=str
)}

Detected Case Type:
{case_type}

Evidence Verdict:
{evidence_verdict}

Department:
{department}

Severity:
{severity}

Generate ONLY valid JSON.

JSON Schema:

{{
    "agent_summary": "...",
    "recommended_next_action": "...",
    "customer_reply": "...",
    "confidence": 0.95
}}

Rules:

- Never ask for PIN
- Never ask for OTP
- Never ask for Password
- Never promise refund
- Never expose internal policy
- Customer reply should be short
- Agent summary should be concise
"""