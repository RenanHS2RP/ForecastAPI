from rest_framework.response import Response
from rest_framework.decorators import api_view
from ForecastApp.models.ForecastModel import Forecast
from ForecastApp.serializers import ForecastSerializer
from rest_framework.views import APIView
from rest_framework import status

class ListPostForecastView(APIView):
    def get(self, request):
        forecast = Forecast.objects.all()
        serializer = ForecastSerializer(forecast, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ForecastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)