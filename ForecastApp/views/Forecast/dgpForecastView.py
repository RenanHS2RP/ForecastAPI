from rest_framework.response import Response
from rest_framework.decorators import api_view
from ForecastApp.models.ForecastModel import Forecast
from ForecastApp.serializers import ForecastSerializer
from rest_framework.views import APIView
from rest_framework import status

class DGPForecastAppView(APIView):
    def delete(self, request, forecast_id):
        try:
            forecast = Forecast.objects.get(pk=forecast_id)
        except Forecast.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        forecast.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, forecast_id):
        try:
            forecast = Forecast.objects.get(pk=forecast_id)
        except Forecast.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ForecastSerializer(forecast)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, forecast_id_id):
        try:
            forecast = Forecast.objects.get(pk=forecast_id_id)
        except Forecast.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ForecastSerializer(forecast, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)