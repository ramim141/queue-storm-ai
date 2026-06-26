import json

from google import genai
from django.conf import settings

from .constants import AI_MODEL
from .prompt_builder import PromptBuilder
from .prompts import SYSTEM_PROMPT


class GeminiService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

        self.builder = PromptBuilder()

    def generate(
        self,
        complaint,
        case_type,
        transaction_history,
        evidence_verdict,
        department,
        severity,
    ):

        prompt = self.builder.build(
            complaint=complaint,
            transaction_history=transaction_history,
            case_type=case_type,
            evidence_verdict=evidence_verdict,
            department=department,
            severity=severity,
        )

        response = self.client.models.generate_content(
            model=AI_MODEL,
            contents=SYSTEM_PROMPT + "\n\n" + prompt,
        )

        text = response.text.strip()

        text = (
            text.replace("```json", "")
                .replace("```", "")
                .strip()
        )

        return json.loads(text)