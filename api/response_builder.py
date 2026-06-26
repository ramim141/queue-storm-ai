class ResponseBuilder:

    def build(
        self,
        ticket_id,
        relevant_transaction_id,
        evidence_verdict,
        case_type,
        severity,
        department,
        agent_summary,
        recommended_next_action,
        customer_reply,
        human_review_required,
        confidence,
        reason_codes,
    ):

        return {
            "ticket_id": ticket_id,
            "relevant_transaction_id": relevant_transaction_id,
            "evidence_verdict": evidence_verdict,
            "case_type": case_type,
            "severity": severity,
            "department": department,
            "agent_summary": agent_summary,
            "recommended_next_action": recommended_next_action,
            "customer_reply": customer_reply,
            "human_review_required": human_review_required,
            "confidence": confidence,
            "reason_codes": reason_codes,
        }