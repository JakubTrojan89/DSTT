from django import forms, models

from gijutsu.models import MartialArt, TechniqueType


class MartialArtForm(forms.ModelForm):
    class Meta:
        model = MartialArt
        fields = ['name', 'description']


class TechniqueTypeForm(forms.ModelForm):
    class Meta:
        model = TechniqueType
        fields = ['name', 'description']