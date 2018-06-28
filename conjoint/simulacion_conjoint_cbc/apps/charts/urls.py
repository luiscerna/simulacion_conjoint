from django.urls import path
from .views import HomeView, get_data, ChartData
app_name = "chart"

urlpatterns = [
	path('home/<pk>/', HomeView.as_view(), name="home"),
	path('api/data/', get_data, name="api-date"),
	path('api/chart/data/', ChartData.as_view()),
]
