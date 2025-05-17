from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    patient_nom = serializers.CharField(source='patient.nom', read_only=True)
    patient_prenom = serializers.CharField(source='patient.prenom', read_only=True)

    class Meta:
        model = Data
        fields = ['data', 'type', 'nom', 'prenom']