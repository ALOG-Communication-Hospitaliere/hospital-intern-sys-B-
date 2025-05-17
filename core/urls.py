from django.urls import path
from .views import get_patient_data

urlpatterns = [
    path('get-data', get_patient_data, name='get_data'),
]