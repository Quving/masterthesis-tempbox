# Create your views here.

from rest_framework import generics, permissions

from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer


class MeasurementList(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]


class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
