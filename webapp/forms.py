from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django import forms
import re

from webapp.models import Task


class TaskForm(forms.ModelForm):
    summary = forms.CharField(
        max_length=123,
        validators=[MinLengthValidator(2, message='Малая длина'),
                    MaxLengthValidator(20, message='Максимальная длина 20 символов')])

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')

        if re.match(r'\d', summary):
            raise ValidationError('Не должно начинаться с цифры')

        if Task.objects.filter(summary=summary).exists():
            raise ValidationError('Запись с таким заголовком уже существует')

        return summary