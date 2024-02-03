from rest_framework import serializers
from ForecastApp.models.ForecastModel import Forecast

class ForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forecast
        fields = '__all__'