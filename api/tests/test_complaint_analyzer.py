from django.test import TestCase

from api.complaint_analyzer import ComplaintAnalyzer
from api.enums import CaseType


class ComplaintAnalyzerTest(TestCase):

    def setUp(self):
        self.analyzer = ComplaintAnalyzer()

    # ---------------------------------
    # Wrong Transfer
    # ---------------------------------

    def test_wrong_transfer_english(self):
        result = self.analyzer.detect_case_type(
            "I accidentally sent money to the wrong number."
        )

        self.assertEqual(
            result,
            CaseType.WRONG_TRANSFER.value
        )

    def test_wrong_transfer_bangla(self):
        result = self.analyzer.detect_case_type(
            "আমি ভুল নম্বরে টাকা পাঠিয়েছি।"
        )

        self.assertEqual(
            result,
            CaseType.WRONG_TRANSFER.value
        )

    # ---------------------------------
    # Payment Failed
    # ---------------------------------

    def test_payment_failed(self):
        result = self.analyzer.detect_case_type(
            "Payment failed but money deducted."
        )

        self.assertEqual(
            result,
            CaseType.PAYMENT_FAILED.value
        )

    # ---------------------------------
    # Refund
    # ---------------------------------

    def test_refund_request(self):
        result = self.analyzer.detect_case_type(
            "I want a refund."
        )

        self.assertEqual(
            result,
            CaseType.REFUND_REQUEST.value
        )

    # ---------------------------------
    # Duplicate Payment
    # ---------------------------------

    def test_duplicate_payment(self):
        result = self.analyzer.detect_case_type(
            "I was charged twice."
        )

        self.assertEqual(
            result,
            CaseType.DUPLICATE_PAYMENT.value
        )

    # ---------------------------------
    # Merchant Settlement
    # ---------------------------------

    def test_merchant_settlement_delay(self):
        result = self.analyzer.detect_case_type(
            "Merchant settlement delay."
        )

        self.assertEqual(
            result,
            CaseType.MERCHANT_SETTLEMENT_DELAY.value
        )

    # ---------------------------------
    # Cash In
    # ---------------------------------

    def test_cash_in_issue(self):
        result = self.analyzer.detect_case_type(
            "Cash in failed."
        )

        self.assertEqual(
            result,
            CaseType.AGENT_CASH_IN_ISSUE.value
        )

    # ---------------------------------
    # Phishing
    # ---------------------------------

    def test_phishing(self):
        result = self.analyzer.detect_case_type(
            "Someone asked for my OTP."
        )

        self.assertEqual(
            result,
            CaseType.PHISHING.value
        )

    # ---------------------------------
    # Unknown
    # ---------------------------------

    def test_unknown_case(self):
        result = self.analyzer.detect_case_type(
            "Hello, nice to meet you."
        )

        self.assertEqual(
            result,
            CaseType.OTHER.value
        )