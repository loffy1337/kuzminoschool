from django.contrib import admin

# Импорт модели школьных предметов
from .models import SchoolSubject
# Импорт моделей материалов для обучения
from .models import MaterialForStudy, ThemesMaterialsForStudy, FileTheme, StudentAnswer, FavouritesForStudy
# Импорт моделей методических материалов
from .models import MethodicalMaterial, ThemesMethodicalMaterials, FileMethodicalTheme, FavouritesMethodical

@admin.register(SchoolSubject)
class SchoolSubjectAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели шокльного предмета"""
    list_display = ('id', 'name', 'subject_class', 'teacher')
    list_display_links = ('name', 'subject_class',)
    search_fields = ('name__startswith',)

@admin.register(MaterialForStudy)
class MaterialForStudyAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели материалов для обучения"""
    list_display = ('id', 'name', 'school_subject',)
    list_display_links = ('name',)
    search_fields = ('name__startswith',)

@admin.register(ThemesMaterialsForStudy)
class ThemesMaterialsForStudyAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели темы материалов для обучения"""
    list_display = ('id', 'name', 'material_for_study',)
    list_display_links = ('name',)
    search_fields = ('name__startswith',)
    prepopulated_fields = {"slug": ("name", )}

@admin.register(FileTheme)
class FileThemeAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели файлов материалов для обучения"""
    list_display = ('id', 'theme', 'file',)
    list_display_links = ('theme',)
    search_fields = ('theme__startswith',)

@admin.register(StudentAnswer)
class StudentAnswerAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели ответа ученика материалов для обучения"""
    list_display = ('id', 'student', 'theme', 'file')
    list_display_links = ('student', 'theme',)
    search_fields = ('student__startswith',)

@admin.register(MethodicalMaterial)
class MethodicalMaterialAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели методических материалов"""
    list_display = ('id', 'name', 'school_subject',)
    list_display_links = ('name',)
    search_fields = ('name__startswith',)

@admin.register(ThemesMethodicalMaterials)
class ThemesMethodicalMaterialsAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели темы методических материалов"""
    list_display = ('id', 'name', 'material_methodical')
    list_display_links = ('name',)
    search_fields = ('name__startswith',)
    prepopulated_fields = {"slug": ("name", )}

@admin.register(FileMethodicalTheme)
class FileMethodicalThemeAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели файла методических материалов"""
    list_display = ('id', 'theme', 'file',)
    list_display_links = ('theme',)
    search_fields = ('theme__startswith',)

@admin.register(FavouritesForStudy)
class FavouritesForStudyAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели избранных материалов для обучения"""
    list_display = ('student', 'material',)
    list_display_links = ('student', 'material',)

@admin.register(FavouritesMethodical)
class FavouritesMethodicalAdmin(admin.ModelAdmin):
    """Класс описывающий вид и дополнительные виджеты для модели избранных методических материалов"""
    list_display = ('student', 'material',)
    list_display_links = ('student', 'material',)
