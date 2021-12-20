from django.contrib import admin

# Register your models here.
from measurements.models import Measurement

admin.site.register(Measurement)
