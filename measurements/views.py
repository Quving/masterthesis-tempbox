# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import generics, permissions

from measurements.filters import MeasurementFilter
from measurements.models import Measurement
from measurements.serializers import MeasurementSerializer


class MeasurementList(generics.ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MeasurementFilter


class MeasurementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
