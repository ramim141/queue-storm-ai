from .enums import CaseType


class ComplaintAnalyzer:

    CASE_PATTERNS = {

        CaseType.WRONG_TRANSFER.value: [
            # English
            "wrong number",
            "wrong recipient",
            "sent to wrong",
            "accidentally sent",
            "mistakenly sent",

            # Banglish
            "vul number",
            "wrong numbere",
            "vul recipient",
            "vul account",

            # Bangla
            "ভুল নম্বরে",
            "ভুল নাম্বারে",
            "ভুল ব্যক্তিকে",
            "ভুল অ্যাকাউন্টে"
        ],

        CaseType.PAYMENT_FAILED.value: [
            "payment failed",
            "money deducted",
            "transaction failed",

            "payment fail",
            "taka kete geche",

            "পেমেন্ট ব্যর্থ",
            "টাকা কেটে গেছে",
            "লেনদেন ব্যর্থ"
        ],

        CaseType.REFUND_REQUEST.value: [
            "refund",
            "refund chai",
            "রিফান্ড",
            "ফেরত চাই"
        ],

        CaseType.DUPLICATE_PAYMENT.value: [
            "charged twice",
            "duplicate payment",
            "double payment",
            "দুইবার কেটেছে",
            "দুইবার টাকা কেটেছে"
        ],

        CaseType.MERCHANT_SETTLEMENT_DELAY.value: [
            "merchant settlement",
            "settlement delay",
            "merchant payment",
            "মার্চেন্ট সেটেলমেন্ট"
        ],

        CaseType.AGENT_CASH_IN_ISSUE.value: [
            "cash in",
            "cashin",
            "agent cash in",
            "ক্যাশ ইন"
        ],

        CaseType.PHISHING.value: [
            "otp",
            "pin",
            "password",
            "verification code",

            "otp dise",
            "pin dise",

            "ওটিপি",
            "পিন",
            "পাসওয়ার্ড"
        ]
    }

    def detect_case_type(self, complaint):

        complaint = complaint.lower().strip()

        for case_type, keywords in self.CASE_PATTERNS.items():
            for keyword in keywords:
                if keyword.lower() in complaint:
                    return case_type

        return CaseType.OTHER.value