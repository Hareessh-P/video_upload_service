from django.contrib import admin
from .models import Course, Video, UserMetadata

admin.site.register(Course)
admin.site.register(Video)
admin.site.register(UserMetadata)
