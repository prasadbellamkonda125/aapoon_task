from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from rest_framework import viewsets, status
from .models import Teacher_Directory
from .serializers import TeacherSerializer


class TeacherModelViewSet(viewsets.ModelViewSet):
    queryset = Teacher_Directory.objects.all()
    serializer_class = TeacherSerializer


@login_required
def import_teachers(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("File is not CSV type")

        df = pd.read_csv(csv_file)
        list_of_dict = df.to_dict(orient='records')
        objs = [
            Teacher_Directory(
                first_name=row['First Name'],
                last_name=row['Last Name'],
                profile_picture=row['Profile picture'],
                email=row['Email Address'],
                phone_number=row['Phone Number'],
                room_number=row['Room Number'],
                subjects=row['Subjects taught']

            )
            for row in list_of_dict

        ]
        try:
            Teacher_Directory.objects.bulk_create(objs)
        except Exception as error:
            return render(request, 'error.html', {"error": str(error)})
        else:
            return HttpResponse("<h1>Data imported successfully<h1>")

    else:
        return render(request, 'import_teachers.html')


def user_logout(request):
    return render(request, 'logout.html')
