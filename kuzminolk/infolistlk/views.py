from django.shortcuts import render

from mainlk.models import Teacher

def teachers_list(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
    }
    return render(request, 'infolistlk/teacher_list.html', context)

# def events_list(request):
    
