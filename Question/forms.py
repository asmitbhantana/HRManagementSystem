from django.forms import ModelForm, BaseInlineFormSet
from Question.models import Question


class QuestionCreateForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option']
