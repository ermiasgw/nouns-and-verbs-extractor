from django.contrib import admin
from django.urls import path
from extractor.views import UploadView, extractedDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', extractedDataView, name='extracted_data'),
    path('api/', UploadView.as_view(), name='api'),
]