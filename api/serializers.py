from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    transaction_id = serializers.CharField()

    timestamp = serializers.DateTimeField()

    type = serializers.ChoiceField(
        choices=[
            "transfer",
            "payment",
            "cash_in",
            "cash_out",
            "settlement",
            "refund",
        ]
    )

    amount = serializers.FloatField(
        min_value=0
    )

    counterparty = serializers.CharField()

    status = serializers.ChoiceField(
        choices=[
            "completed",
            "failed",
            "pending",
            "reversed",
        ]
    )


class TicketSerializer(serializers.Serializer):

    ticket_id = serializers.CharField()

    complaint = serializers.CharField()

    language = serializers.ChoiceField(
        choices=[
            "en",
            "bn",
            "banglish",
            "mixed",
        ],
        required=False,
        default="mixed",
    )

    channel = serializers.ChoiceField(
        choices=[
            "mobile_app",
            "web",
            "in_app_chat",
            "call_center",
            "email",
            "merchant_portal",
            "field_agent",
        ],
        required=False,
        default="mobile_app",
    )

    user_type = serializers.ChoiceField(
        choices=[
            "customer",
            "merchant",
            "agent",
            "unknown",
        ],
        required=False,
        default="customer",
    )

    campaign_context = serializers.CharField(
        required=False,
        allow_blank=True,
        default="",
    )

    transaction_history = TransactionSerializer(
        many=True,
        required=False,
        default=list,
    )

    metadata = serializers.DictField(
        required=False,
        default=dict,
    )