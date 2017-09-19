from django import forms

from .models import Publicar

class PostForm(forms.ModelForm):

    class Meta:
        model = Publicar
        fields = ('titulo', 'texto',)
