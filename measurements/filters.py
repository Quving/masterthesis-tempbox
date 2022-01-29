from django_filters import rest_framework as filters

from measurements.models import Measurement


class MeasurementFilter(filters.FilterSet):
    min_timestamp = filters.NumberFilter(field_name="timestamp", lookup_expr='gte')
    max_timestamp = filters.NumberFilter(field_name="timestamp", lookup_expr='lte')

    min_temperature = filters.NumberFilter(field_name="temperature", lookup_expr='gte')
    max_temperature = filters.NumberFilter(field_name="temperature", lookup_expr='lte')

    class Meta:
        model = Measurement
        fields = [
            'station_id',
            'source',
            'city',
            'country',
            'lat',
            'lng',
            'altitude',
            'min_timestamp',
            'max_timestamp',
            'min_temperature',
            'max_temperature',
        ]
