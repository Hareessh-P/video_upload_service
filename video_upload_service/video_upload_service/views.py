from rest_framework import generics
from .models import Course, UserMetadata, Video
from .serializers import CourseSerializer, UserMetadataSerializer, VideoSerializer

### COURSE

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        # Set the instructor as the currently logged-in user
        serializer.save(instructor=self.request.user)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

### USER

class UserMetadataView(generics.RetrieveUpdateAPIView):
    queryset = UserMetadata.objects.all()
    serializer_class = UserMetadataSerializer

    def perform_update(self, serializer):
        serializer.save()

### VIDEO

class VideoListView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        # Set the course for the video based on the request data
        course_id = self.request.data.get('course')
        course = Course.objects.get(pk=course_id)
        serializer.save(course=course)

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
