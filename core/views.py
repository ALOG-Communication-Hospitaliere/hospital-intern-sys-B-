from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient, Data
from .serializers import DataSerializer  
@api_view(['POST'])
def get_patient_data(request):
    num = request.data.get('num')
    data_type = request.data.get('type')

    try:
        patient = Patient.objects.get(num=num)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)

    data = Data.objects.filter(patient=patient, type=data_type)
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)