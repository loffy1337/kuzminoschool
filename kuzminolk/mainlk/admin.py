from django.contrib import admin

from .models import Teacher, Student, SchoolSubjectForList

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели учителя"""
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name__startswith',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели ученика"""
    list_display = ('id','name', 'student_class')
    list_display_links = ('name',)
    list_filter = ('student_class',)
    search_fields = ('name__startswith',)

@admin.register(SchoolSubjectForList)
class SchoolSubjectForListAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели школьного предмета"""
    list_display = ('id','name', 'teacher')
    list_display_links = ('name',)
    search_fields = ('name__startswith',)
