# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserMetadata(AbstractUser):
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    bio = models.TextField()
    profile_picture_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Specify unique related names for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_metadata_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_metadata_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    instructor = models.ForeignKey(UserMetadata, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Video(models.Model):
    video_title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    video_url = models.CharField(max_length=255)
    thumbnail_url = models.CharField(max_length=255)
    duration_seconds = models.IntegerField()
    resolution_width = models.IntegerField()
    resolution_height = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)