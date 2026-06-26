from rest_framework.test import APITestCase
from rest_framework import status


class AnalyzeAPITest(APITestCase):

    def test_health_endpoint(self):

        response = self.client.get("/api/health/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_wrong_transfer(self):

        payload = {
            "ticket_id": "TEST-001",
            "complaint": "I sent 5000 taka to wrong number.",
            "transaction_history": [
                {
                    "transaction_id": "TXN-001",
                    "timestamp": "2026-04-14T10:00:00Z",
                    "type": "transfer",
                    "amount": 5000,
                    "counterparty": "01712345678",
                    "status": "completed"
                }
            ]
        }

        response = self.client.post(
            "/api/analyze-ticket/",
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["case_type"],
            "wrong_transfer"
        )

    def test_payment_failed(self):

        payload = {
            "ticket_id": "TEST-002",
            "complaint": "Payment failed but money deducted.",
            "transaction_history": [
                {
                    "transaction_id": "TXN-002",
                    "timestamp": "2026-04-14T10:00:00Z",
                    "type": "payment",
                    "amount": 1200,
                    "counterparty": "Daraz",
                    "status": "failed"
                }
            ]
        }

        response = self.client.post(
            "/api/analyze-ticket/",
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data["case_type"],
            "payment_failed"
        )

    def test_invalid_request(self):

        payload = {
            "complaint": "Hello"
        }

        response = self.client.post(
            "/api/analyze-ticket/",
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )