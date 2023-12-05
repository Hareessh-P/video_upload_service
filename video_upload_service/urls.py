# your_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('video_upload_service.urls')),  # Adjust the path as needed
    # Add other URL patterns as needed
]


