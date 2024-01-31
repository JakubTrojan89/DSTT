from django import forms, models
from django.forms import widgets

from gijutsu.models import MartialArt, TechniqueType, Technique, BeltColor, BeltRanking


class MartialArtForm(forms.ModelForm):
    class Meta:
        model = MartialArt
        fields = ['name', 'description']


class TechniqueTypeForm(forms.ModelForm):
    class Meta:
        model = TechniqueType
        fields = ['name', 'description']


class TechniqueForm(forms.ModelForm):
    technique_type = forms.ModelChoiceField(queryset=TechniqueType.objects.all(), empty_label=None)
    martial_art = forms.ModelChoiceField(queryset=MartialArt.objects.all(), empty_label=None)
    class Meta:
        model = Technique
        fields = ['name', 'description', 'technique_type', 'martial_art']


class BeltColorForm(forms.ModelForm):
    class Meta:
        model = BeltColor
        fields = ['color_name', 'martial_art']


class BeltRankingForm(forms.ModelForm):
    class Meta:
        model = BeltRanking
        fields = ['belt_color', 'martial_art', 'technique']
        widgets = {
            'martial_art': forms.Select(),
            'belt_color': forms.CheckboxSelectMultiple()
        }
