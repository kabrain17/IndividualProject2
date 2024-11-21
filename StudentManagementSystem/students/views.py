from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Student
from .serializers import StudentSerializer
from rest_framework.permissions import IsAuthenticated
from StudentManagementSystem.users.permissions import IsAdmin, IsStudent

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]  # Требуется авторизация для всех операций

    @method_decorator(cache_page(60 * 15))  # Кэшируем список на 15 минут
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_permissions(self):
        """Динамическое разграничение прав доступа"""
        if self.action in ['retrieve', 'update', 'partial_update']:
            return [IsStudent()]  # Только студент может просматривать или обновлять свои данные
        elif self.action in ['create', 'destroy']:
            return [IsAdmin()]  # Только администратор может добавлять/удалять студентов
        return super().get_permissions()
