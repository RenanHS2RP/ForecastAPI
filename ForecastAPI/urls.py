"""
URL configuration for ForecastAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ForecastApp.views.Forecast.listPostForecastView import ListPostForecastView
from ForecastApp.views.Forecast.dgpForecastView import DGPForecastAppView
from django.urls import path

urlpatterns = [
    path('forecast/', ListPostForecastView.as_view(), name='Forecast'),
    path('forecast/<str:forecast_id>', DGPForecastAppView.as_view(), name='Forecasts'),
]
