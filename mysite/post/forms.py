from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import User
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=forms.Textarea)
    is_public = forms.BooleanField(widget=forms.NullBooleanSelect)

class updatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','is_public']
        widgets= {
        'body' : Textarea()
        }
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit'
    #     self.helper.add_input(Submit('submit', 'Submit'))

class PostForm(ModelForm):
    class Meta():
        model = Post
        fields = ('title','body','is_public')
        widgets = {
        'body' : Textarea()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit'

        self.helper.add_input(Submit('submit', 'Submit'))
