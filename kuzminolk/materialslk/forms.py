from django import forms

from .models import StudentAnswer, MaterialForStudy

class CreatePartForm(forms.ModelForm):
    """Форма, описывающая создание нового раздела предмета"""
    class Meta:
        model = MaterialForStudy
        fields = ('name',)

class StudentAnswerForm(forms.ModelForm):
    """Форма, описывающая ответ ученика в виде docx файла"""
    class Meta:
        model = StudentAnswer
        fields = ('file',)
