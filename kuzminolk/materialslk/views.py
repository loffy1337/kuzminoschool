from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Импорт моделей школьных предметов
from .models import SchoolSubject
# Импорт моделей материалов для обучения
from .models import MaterialForStudy, ThemesMaterialsForStudy
# Импорт моделей методических материалов
from .models import MethodicalMaterial, ThemesMethodicalMaterials
# Импорт моделей избранных материалов
from .models import FavouritesForStudy, FavouritesMethodical
# Импорт форм
from .forms import StudentAnswerForm, CreatePartForm

@login_required
def for_study(request):
    """Представление списка школьных предметов (Материалы для обучения)"""
    try: school_subjects = SchoolSubject.objects.filter(teacher=request.user.teacher.pk)
    except: school_subjects = SchoolSubject.objects.filter(subject_class=request.user.student.student_class)
    finally:
        context = {'school_subjects': school_subjects}
        return render(request, 'materialslk/materials_for_study.html', context)

@login_required
def for_study_parts(request, subject_id):
    """Представление списка разделов и их тем (Материалы для обучения)"""
    materials = MaterialForStudy.objects.filter(school_subject=subject_id)
    school_subject = SchoolSubject.objects.get(pk=subject_id)
    try:
        if request.user.student.student_class == school_subject.subject_class:
            context = {
                'materials': materials,
                'subject_id': subject_id,
                'is_teacher': False,
            }
            return render(request, 'materialslk/materials_for_study_parts.html', context)
    except:
        if request.user.teacher == school_subject.teacher:
            if request.method == 'POST':
                form = CreatePartForm(request.POST)
                if form.is_valid():
                    object = form.save(commit=False)
                    object.school_subject = school_subject
                    form.save(commit=True)
            else: form = CreatePartForm()
            context = {
                'form': form,
                'materials': materials,
                'subject_id': subject_id,
                'is_teacher': True,
            }
            return render(request, 'materialslk/materials_for_study_parts.html', context)  
    return render(request, 'http_error.html', {'message': 'Вы не имеете доступ к данной странице!'})

@login_required
def for_study_detail(request, theme_slug):
    """Представление детального просмотра темы (Материалы для обучения)"""
    theme = ThemesMaterialsForStudy.objects.get(slug=theme_slug)
    try:
        if request.user.student.student_class == theme.material_for_study.school_subject.subject_class:
            if request.method == 'POST':
                form = StudentAnswerForm(request.POST, request.FILES)
                if form.is_valid():
                    object = form.save(commit=False)
                    object.student = request.user.student
                    object.theme = theme
                    form.save(commit=True)
            else: form = StudentAnswerForm()
            context = {
                'theme': theme,
                'form': form,
                'is_teacher': False,
            }
            return render(request, 'materialslk/materials_for_study_detail.html', context)
    except:
        if request.user.teacher == theme.material_for_study.school_subject.teacher:
            context = {
                'theme': theme,
                'is_teacher': True,
            }
            return render(request, 'materialslk/materials_for_study_detail.html', context)
    return render(request, 'http_error.html', {'message': 'Вы не имеете доступ к данной странице!'})

@login_required
def methodical(request):
    """Представление списка школьных предметов (Методические материалы)"""
    try: school_subjects = SchoolSubject.objects.filter(teacher=request.user.teacher.pk)
    except: school_subjects = SchoolSubject.objects.filter(subject_class=request.user.student.student_class)
    finally:
        context = {'school_subjects': school_subjects}
        return render(request, 'materialslk/materials_methodical.html', context)

@login_required
def methodical_parts(request, subject_id):
    """Представление списка разделов и их тем (Методические материалы)"""
    materials = MethodicalMaterial.objects.filter(school_subject=subject_id)
    try:
        if request.user.student.student_class == SchoolSubject.objects.get(pk=subject_id).subject_class:
            context = {
                'materials': materials,
                'subject_id': subject_id,
                'is_teacher': False,
            }
            return render(request, 'materialslk/materials_methodical_parts.html', context)
    except:
        if request.user.teacher == SchoolSubject.objects.get(pk=subject_id).teacher:
            context = {
                'materials': materials,
                'subject_id': subject_id,
                'is_teacher': True,
            }
            return render(request, 'materialslk/materials_methodical_parts.html', context)  
    return render(request, 'http_error.html', {'message': 'Вы не имеете доступ к данной странице!'})

@login_required
def methodical_detail(request, theme_slug):
    """Представление детального просмотра темы (Методические материалы)"""
    theme = ThemesMethodicalMaterials.objects.get(slug=theme_slug)
    try:
        if request.user.student.student_class == theme.material_methodical.school_subject.subject_class:
            context = {
                'theme': theme,
                'is_teacher': False,
            }
            return render(request, 'materialslk/materials_methodical_detail.html', context)
    except:
        if request.user.teacher == theme.material_methodical.school_subject.teacher:
            context = {
                'theme': theme,
                'is_teacher': True,
            }
            return render(request, 'materialslk/materials_methodical_detail.html', context)
    return render(request, 'http_error.html', {'message': 'Вы не имеете доступ к данной странице!'})

@login_required
def favourites_add(request, type_of_material, theme_slug):
    """Представление добавляющее материалы в избранное пользователя"""
    if type_of_material == 'for_study':
        if not FavouritesForStudy.objects.filter(student=request.user.student, material=ThemesMaterialsForStudy.objects.get(slug=theme_slug)).first():
            FavouritesForStudy.objects.create(student=request.user.student, material=ThemesMaterialsForStudy.objects.get(slug=theme_slug))
        return redirect('for_study_detail', theme_slug=theme_slug)
    elif type_of_material == 'methodical':
        if not FavouritesMethodical.objects.filter(student=request.user.student, material=ThemesMethodicalMaterials.objects.get(slug=theme_slug)).first():
            FavouritesMethodical.objects.create(student=request.user.student, material=ThemesMethodicalMaterials.objects.get(slug=theme_slug))
        return redirect('methodical_detail', theme_slug=theme_slug)
    raise Http404

@login_required
def favourites(request):
    """Представление списка избранных материалов"""
    try:
        materials_for_study = FavouritesForStudy.objects.filter(student=request.user.student)
        materials_methodical = FavouritesMethodical.objects.filter(student=request.user.student)
        context = {
            'for_study': materials_for_study,
            'methodical': materials_methodical,
        }
        return render(request, 'materialslk/favourites.html', context)
    except:
        return render(request, 'http_error.html', {'message': 'Доступ к данной странице имеют только ученики!'})
