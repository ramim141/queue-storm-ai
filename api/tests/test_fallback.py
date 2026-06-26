from unittest.mock import patch

from rest_framework.test import APITestCase


class GeminiFallbackTest(APITestCase):

    URL = "/api/analyze-ticket/"

    @patch("api.services.GeminiService.generate")
    def test_gemini_failure(self, mock_generate):

        mock_generate.side_effect = Exception(
            "Gemini Down"
        )

        payload = {

            "ticket_id": "FAIL-001",

            "complaint": "Wrong transfer",

            "transaction_history": []

        }

        response = self.client.post(
            self.URL,
            payload,
            format="json"
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertEqual(
            response.data["confidence"],
            0.5
        )