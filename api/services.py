from .transaction_matcher import TransactionMatcher
from .complaint_analyzer import ComplaintAnalyzer
from .routing_engine import RoutingEngine
from .llm import GeminiService
from .safety_engine import SafetyEngine
from .response_builder import ResponseBuilder
from .evidence_engine import EvidenceEngine
from .duplicate_detector import DuplicatePaymentDetector
from .logger import logger
from .fallback import get_fallback_response
from .enums import CaseType, EvidenceVerdict


class AnalyzeService:

    def __init__(self):
        self.analyzer = ComplaintAnalyzer()
        self.matcher = TransactionMatcher()
        self.router = RoutingEngine()
        self.llm = GeminiService()
        self.builder = ResponseBuilder()
        self.evidence = EvidenceEngine()
        self.safety = SafetyEngine()
        self.duplicate_detector = DuplicatePaymentDetector()

    def analyze(self, data):

        logger.info(f"Analyzing Ticket: {data['ticket_id']}")

        complaint = data["complaint"]
        transaction_history = data.get("transaction_history", [])

        # -----------------------------
        # Detect Complaint Type
        # -----------------------------
        case_type = self.analyzer.detect_case_type(
            complaint
        )

        route = self.router.get_route(
            case_type
        )

        # -----------------------------
        # Match Transaction
        # -----------------------------
        matched_transaction = self.matcher.find_match(
            complaint,
            transaction_history
        )

        relevant_transaction_id = (
            matched_transaction["transaction_id"]
            if matched_transaction
            else None
        )

        # -----------------------------
        # Duplicate Detection
        # -----------------------------
        (
            case_type,
            route,
            relevant_transaction_id,
            evidence,
        ) = self._handle_duplicate(
            case_type,
            route,
            relevant_transaction_id,
            transaction_history,
            complaint,
            matched_transaction,
        )

        evidence_verdict = evidence["verdict"]

        logger.info(f"Case Type: {case_type}")
        logger.info(f"Evidence Verdict: {evidence_verdict}")

        # -----------------------------
        # AI Response
        # -----------------------------
        try:

            ai = self._generate_ai_response(
                complaint=complaint,
                case_type=case_type,
                transaction_history=transaction_history,
                evidence_verdict=evidence_verdict,
                route=route,
            )

        except Exception as e:

            logger.warning(
                f"Gemini unavailable. Using fallback. Error: {e}"
            )

            ai = get_fallback_response(
                case_type=case_type
            )

        # -----------------------------
        # Build Final Response
        # -----------------------------
        result = self.builder.build(
            ticket_id=data["ticket_id"],
            relevant_transaction_id=relevant_transaction_id,
            evidence_verdict=evidence_verdict,
            case_type=case_type,
            severity=route["severity"],
            department=route["department"],
            agent_summary=ai["agent_summary"],
            recommended_next_action=ai["recommended_next_action"],
            customer_reply=ai["customer_reply"],
            human_review_required=route["human_review_required"],
            confidence=ai["confidence"],
            reason_codes=evidence["reason_codes"],
        )

        logger.info(f"Completed Ticket: {data['ticket_id']}")

        return result

    # ====================================================
    # Duplicate Detection
    # ====================================================

    def _handle_duplicate(
        self,
        case_type,
        route,
        relevant_transaction_id,
        transaction_history,
        complaint,
        matched_transaction,
    ):

        duplicate = self.duplicate_detector.detect(
            transaction_history
        )

        if duplicate:

            logger.info("Duplicate payment detected.")

            case_type = CaseType.DUPLICATE_PAYMENT.value

            route = self.router.get_route(
                case_type
            )

            relevant_transaction_id = duplicate[
                "transaction_id"
            ]

            evidence = {
                "verdict": EvidenceVerdict.CONSISTENT.value,
                "reason_codes": [
                    "duplicate_payment_detected"
                ]
            }

        else:

            evidence = self.evidence.evaluate(
                complaint,
                matched_transaction
            )

        return (
            case_type,
            route,
            relevant_transaction_id,
            evidence,
        )

    # ====================================================
    # AI Response
    # ====================================================

    def _generate_ai_response(
        self,
        complaint,
        case_type,
        transaction_history,
        evidence_verdict,
        route,
    ):

        ai = self.llm.generate(
            complaint=complaint,
            case_type=case_type,
            transaction_history=transaction_history,
            evidence_verdict=evidence_verdict,
            department=route["department"],
            severity=route["severity"],
        )

        return self.safety.sanitize(ai)