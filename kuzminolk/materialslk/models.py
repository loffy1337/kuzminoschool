import os
from django.db import models
from django.shortcuts import reverse

# Импорт моделей ученика и учителя
from mainlk.models import Student, Teacher

class SchoolSubject(models.Model):
    """Класс описывающий таблицу школьных предметов имеет: название, класс, ссылку на учителя"""
    CLASS_CHOICE = [
        (1, 1), (2, 2), (3, 3),
        (4, 4), (5, 5), (6, 6),
        (7, 7), (8, 8), (9, 9),
    ]

    name = models.CharField(
        max_length=80,
        verbose_name='Наименование предмета'
    )
    subject_class = models.PositiveSmallIntegerField(
        choices=CLASS_CHOICE,
        verbose_name='Класс предмета'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Учитель',
    )

    class Meta:
        verbose_name = 'Школьный предмет'
        verbose_name_plural = 'Школьные предметы'
        ordering = ('subject_class',)

    def __str__(self):
        return f'{self.name} ({self.subject_class} класс)'

class MaterialForStudy(models.Model):
    """Класс описывающий таблицу разделов для материалов имеет: ссылку на учителя, ссылку на школьный предмет, наименование"""
    school_subject = models.ForeignKey(
        SchoolSubject,
        on_delete=models.CASCADE,
        verbose_name='Школьный предмет'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование раздела'
    )

    class Meta:
        verbose_name = 'Раздел (Материалы для обучения)'
        verbose_name_plural = 'Разделы (Материалы для обучения)'

    def __str__(self):
        return f'Раздел: {self.name} ({self.school_subject})'

class ThemesMaterialsForStudy(models.Model):
    """Класс описывающий таблицу тем для разделов имеет: ссылку на раздел, наименование, слаг, текст темы"""
    material_for_study = models.ForeignKey(
        MaterialForStudy,
        on_delete=models.CASCADE,
        verbose_name='Раздел материала'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Наменование темы'
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name='Слаг темы'
    )
    text = models.TextField(
        verbose_name='Текст темы'
    )

    class Meta:
        verbose_name = 'Тема (Материалы для обучения)'
        verbose_name_plural = 'Темы (Материалы для обучения)'

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('for_study_detail', kwargs={'theme_slug': self.slug})

class FileTheme(models.Model):
    """Класс описывающий таблицу файл темы имеет: ссылку на раздел, наименование, файл"""
    theme = models.ForeignKey(
        ThemesMaterialsForStudy,
        on_delete=models.CASCADE,
        verbose_name='Тема'
    )
    file = models.FileField(
        upload_to='materials_files/%Y/%m/%d/',
        verbose_name='Файл темы'
    )
    
    class Meta:
        verbose_name = 'Файл (Материалы для обучения)'
        verbose_name_plural = 'Файлы (Материалы для обучения)'

    def __str__(self):
        file_name = os.path.basename(str(self.file))
        return f'{file_name}'

class StudentAnswer(models.Model):
    """Класс описывающий таблицу ответов ученика на тему имеет: студента, тему, файл, комментарий"""
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Ученик'
    )
    theme = models.ForeignKey(
        ThemesMaterialsForStudy,
        on_delete=models.CASCADE,
        verbose_name='Тема'
    )
    file = models.FileField(
        upload_to='students_files/%Y/%m/%d/',
        verbose_name='Файл ответа студента'
    )

    class Meta:
        verbose_name = 'Ответ студента (Материалы для обучения)'
        verbose_name_plural = 'Ответы студентов (Материалы для обучения)'

    def __str__(self):
        return f'Ответ от: {self.student} на тему: {self.theme}'

class MethodicalMaterial(models.Model):
    """Класс описывающий таблицу разделов для методических материалов имеет: ссылку на учителя, ссылку на школьный предмет, наименование"""
    school_subject = models.ForeignKey(
        SchoolSubject,
        on_delete=models.CASCADE,
        verbose_name='Школьный предмет'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование раздела'
    )

    class Meta:
        verbose_name = 'Раздел (Методические материалы)'
        verbose_name_plural = 'Разделы (Методические материалы)'

    def __str__(self):
        return f'Раздел: {self.name}'

class ThemesMethodicalMaterials(models.Model):
    """Класс описывающий таблицу тем для разделов имеет: ссылку на раздел, наименование, слаг, текст темы"""
    material_methodical = models.ForeignKey(
        MethodicalMaterial,
        on_delete=models.CASCADE,
        verbose_name='Раздел методического материала'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Наменование темы'
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name='Слаг темы'
    )
    text = models.TextField(
        verbose_name='Текст темы'
    )

    class Meta:
        verbose_name = 'Тема (Методические материалы)'
        verbose_name_plural = 'Темы (Методические материалы)'

    def __str__(self):
        return f'Тема: {self.name}'

    def get_absolute_url(self):
        return reverse('methodical_detail', kwargs={'theme_slug': self.slug})

class FileMethodicalTheme(models.Model):
    """Класс описывающий таблицу файл темы имеет: ссылку на раздел, наименование, слаг, текст темы"""
    theme = models.ForeignKey(
        ThemesMethodicalMaterials,
        on_delete=models.CASCADE,
        verbose_name='Тема'
    )
    file = models.FileField(
        upload_to='materials_files/%Y/%m/%d/',
        verbose_name='Файл темы'
    )
    
    class Meta:
        verbose_name = 'Файл (Методические материалы)'
        verbose_name_plural = 'Файлы (Методические материалы)'

    def __str__(self):
        file_name = os.path.basename(str(self.file))
        return f'{file_name}'

class FavouritesForStudy(models.Model):
    """Класс описывающий таблицу избранных материалов для обучения имеет: ссылку на ученика, ссылку на тему"""
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    material = models.ForeignKey(
        ThemesMaterialsForStudy,
        on_delete=models.CASCADE,
        verbose_name='Ссылка на материал'
    )

    class Meta:
        verbose_name = 'Избранное (Материалы для обучения)'
        verbose_name_plural = 'Избранные (Материалы для обучения)'
        constraints = [
            models.UniqueConstraint(fields=['student', 'material'], name='unique_student_material_for_study')
        ]

    def __str__(self):
        return f'{self.material.name}'

class FavouritesMethodical(models.Model):
    """Класс описывающий таблицу избранных методических материалов: ссылку на ученика, ссылку на тему"""
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    material = models.ForeignKey(
        ThemesMethodicalMaterials,
        on_delete=models.CASCADE,
        verbose_name='Ссылка на материал'
    )

    class Meta:
        verbose_name = 'Избранное (Методические материалы)'
        verbose_name_plural = 'Избранные (Методические материалы)'
        constraints = [
            models.UniqueConstraint(fields=['student', 'material'], name='unique_student_material_methodical')
        ]

    def __str__(self):
        return f'{self.material.name}'
