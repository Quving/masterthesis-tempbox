from rest_framework import serializers

from measurements.models import Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Measurement
        fields = '__all__'
