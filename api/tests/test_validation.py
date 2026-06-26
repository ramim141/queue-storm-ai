from rest_framework.test import APITestCase
from rest_framework import status


class ValidationTest(APITestCase):

    URL = "/api/analyze-ticket/"

    def test_missing_ticket_id(self):

        payload = {
            "complaint": "Wrong transfer"
        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_missing_complaint(self):

        payload = {
            "ticket_id": "TKT-001"
        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_invalid_language(self):

        payload = {
            "ticket_id": "TKT-001",
            "complaint": "Wrong transfer",
            "language": "japanese"
        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_invalid_channel(self):

        payload = {
            "ticket_id": "TKT-001",
            "complaint": "Wrong transfer",
            "channel": "facebook"
        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_invalid_user_type(self):

        payload = {
            "ticket_id": "TKT-001",
            "complaint": "Wrong transfer",
            "user_type": "admin"
        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_negative_amount(self):

        payload = {
            "ticket_id": "TKT-001",
            "complaint": "Wrong transfer",

            "transaction_history": [
                {
                    "transaction_id": "TXN-001",
                    "timestamp": "2026-04-14T10:00:00Z",
                    "type": "transfer",
                    "amount": -500,
                    "counterparty": "01711111111",
                    "status": "completed"
                }
            ]
        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )