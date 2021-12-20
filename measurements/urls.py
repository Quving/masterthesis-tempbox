from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from measurements import views

urlpatterns = [
    path('measurements/', views.MeasurementList.as_view()),
    path('measurements/<int:pk>', views.MeasurementDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
