from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsStudent, IsTeacher, IsAdmin  # Импорт кастомных разрешений
from .models import Student
from StudentManagementSystem.students.serializers import StudentSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]  # Базовая проверка на авторизацию

    def get_permissions(self):
        """Динамически определяем разрешения"""
        if self.action in ['retrieve', 'update', 'partial_update']:
            return [IsStudent()]  # Только студент может редактировать свои данные
        elif self.action in ['create', 'destroy']:
            return [IsAdmin()]  # Только администратор может добавлять или удалять студентов
        return super().get_permissions()
