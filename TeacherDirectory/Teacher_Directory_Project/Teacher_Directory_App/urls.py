from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import import_teachers, TeacherModelViewSet, user_logout

router = routers.DefaultRouter()

router.register(r"teacher-view", TeacherModelViewSet, basename="teacher-view")

urlpatterns = [
    path("", include(router.urls)),
    path('export_data', import_teachers),
    path('logout/', user_logout)

]