from datetime import datetime, timedelta

from django.test import TestCase

from api.duplicate_detector import DuplicatePaymentDetector


class DuplicatePaymentDetectorTest(TestCase):

    def setUp(self):
        self.detector = DuplicatePaymentDetector()

        self.base_time = datetime(
            2026,
            6,
            26,
            10,
            0,
            0
        )

    def test_duplicate_payment_detected(self):

        transactions = [
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            },
            {
                "transaction_id": "TXN-002",
                "timestamp": self.base_time + timedelta(minutes=2),
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            }
        ]

        result = self.detector.detect(transactions)

        self.assertIsNotNone(result)
        self.assertTrue(result["duplicate"])
        self.assertEqual(
            result["transaction_id"],
            "TXN-002"
        )

    def test_single_transaction(self):

        transactions = [
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            }
        ]

        self.assertIsNone(
            self.detector.detect(transactions)
        )

    def test_empty_transactions(self):

        self.assertIsNone(
            self.detector.detect([])
        )

    def test_different_amount(self):

        transactions = [
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            },
            {
                "transaction_id": "TXN-002",
                "timestamp": self.base_time + timedelta(minutes=1),
                "type": "payment",
                "amount": 700,
                "counterparty": "merchant_a"
            }
        ]

        self.assertIsNone(
            self.detector.detect(transactions)
        )

    def test_different_counterparty(self):

        transactions = [
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            },
            {
                "transaction_id": "TXN-002",
                "timestamp": self.base_time + timedelta(minutes=1),
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_b"
            }
        ]

        self.assertIsNone(
            self.detector.detect(transactions)
        )

    def test_different_transaction_type(self):

        transactions = [
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            },
            {
                "transaction_id": "TXN-002",
                "timestamp": self.base_time + timedelta(minutes=1),
                "type": "transfer",
                "amount": 500,
                "counterparty": "merchant_a"
            }
        ]

        self.assertIsNone(
            self.detector.detect(transactions)
        )

    def test_outside_duplicate_window(self):

        transactions = [
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            },
            {
                "transaction_id": "TXN-002",
                "timestamp": self.base_time + timedelta(minutes=30),
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            }
        ]

        self.assertIsNone(
            self.detector.detect(transactions)
        )

    def test_unsorted_transactions(self):

        transactions = [
            {
                "transaction_id": "TXN-002",
                "timestamp": self.base_time + timedelta(minutes=2),
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            },
            {
                "transaction_id": "TXN-001",
                "timestamp": self.base_time,
                "type": "payment",
                "amount": 500,
                "counterparty": "merchant_a"
            }
        ]

        result = self.detector.detect(transactions)

        self.assertIsNotNone(result)
        self.assertEqual(
            result["transaction_id"],
            "TXN-002"
        )