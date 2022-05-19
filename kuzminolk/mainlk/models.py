from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    """Класс описывающий таблицу учителя имеет: ссылку на пользователя, ФИО"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    name = models.CharField(
        max_length=250,
        verbose_name='ФИО учителя'
    )
    photo = models.ImageField(
        upload_to='teachers_photos/',
        blank=True,
        verbose_name='Фотография'
    )
    education = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Образование'
    )

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    """Класс описывающий таблицу ученика имеет: ссылку на пользователя, ФИО, класс"""
    CLASS_CHOICE = [
        (1, 1), (2, 2), (3, 3),
        (4, 4), (5, 5), (6, 6),
        (7, 7), (8, 8), (9, 9),
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    name = models.CharField(
        max_length=250,
        verbose_name='ФИО ученика'
    )
    student_class = models.PositiveSmallIntegerField(
        choices=CLASS_CHOICE,
        verbose_name='Класс ученика'
    )

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
        ordering = ('student_class',)

    def __str__(self):
        return f'{self.name}'

class SchoolSubjectForList(models.Model):
    """Класс описывающий таблицу школьных предметов имеет: название, ссылку на учителя"""
    name = models.CharField(
        max_length=80,
        verbose_name='Наименование предмета'
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='Учитель',
    )

    class Meta:
        verbose_name = 'Школьный предмет'
        verbose_name_plural = 'Школьные предметы'

    def __str__(self):
        return f'{self.name}'