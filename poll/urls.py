from . import views
from django.urls import path


urlpatterns = [
    path('', views.fetch_data, name='fetch_data'),
]
