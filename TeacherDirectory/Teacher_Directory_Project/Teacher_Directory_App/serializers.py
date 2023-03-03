from rest_framework.serializers import ModelSerializer
from .models import Teacher_Directory


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher_Directory
        fields = "__all__"
