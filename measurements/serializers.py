from rest_framework import serializers

from measurements.models import Measurement


class MeasurementSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    measurement_id = serializers.CharField(max_length=32)
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    source = serializers.CharField(max_length=64)
    timezone = serializers.CharField(max_length=64)
    timestamp = serializers.IntegerField()
    temperature = serializers.IntegerField()
    country = serializers.CharField(max_length=64)
    city = serializers.CharField(max_length=64)
    street = serializers.CharField(max_length=64)
    altitude = serializers.IntegerField()

    class Meta:
        model = Measurement
        fields = '__all__'
