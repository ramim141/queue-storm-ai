from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import TicketSerializer
from .services import AnalyzeService

class HealthAPIView(APIView):
    def get(self, request):
        return Response({"status": "ok"})


class AnalyzeTicketAPIView(APIView):

    def post(self, request):

        serializer = TicketSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        service = AnalyzeService()

        result = service.analyze(serializer.validated_data)

        return Response(result)