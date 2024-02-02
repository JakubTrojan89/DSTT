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
    technique_type = forms.ModelChoiceField(queryset=TechniqueType.objects.all())
    martial_art = forms.ModelMultipleChoiceField(queryset=MartialArt.objects.all())

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


class MartialArtSearchForm(forms.Form):
    name = forms.CharField(max_length=32, required=False)


class TechniqueSearchForm(forms.Form):
    name = forms.CharField(max_length=64, required=False)
    technique_type = forms.ModelChoiceField(queryset=TechniqueType.objects.all(), empty_label=None)
    martial_art = forms.ModelChoiceField(queryset=MartialArt.objects.all(), empty_label=None)


class MartialArtLegendForm(forms.Form):
    first_name = forms.CharField(max_length=64)
    last_name = forms.CharField(max_length=64)
    martial_art = forms.ModelChoiceField(queryset=MartialArt.objects.all(), empty_label=None)

    def save(self):
        pass


