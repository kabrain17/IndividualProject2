from rest_framework.viewsets import ModelViewSet
from users.permissions import IsAdmin, IsTeacher
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsTeacher()]  # Только учитель может управлять курсами
        return super().get_permissions()
