from django.shortcuts import render, redirect
from django.views import View

from gijutsu.forms import MartialArtForm, TechniqueTypeForm
from gijutsu.models import MartialArt


class MainPageView(View):
    def get(self, request):
        return render(request, 'base.html')

class MartialArtView(View):
    def get(self, request):
        martial_art = ['BJJ', 'Submission Grappling', 'Wrestling', 'Judo']
        return render(request, 'martial_art.html', {'martial_art': martial_art})

class IndexView(View):
    def get(self, request):
        lst = ['bjj', 'submission grappling', 'wrestling', 'judo']
        return render(request, 'index.html', {'lista':lst})

class AddMartialArtView(View):
    template_name = 'add_martial_art.html'
    def get(self, request):
        form = MartialArtForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MartialArtForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'message': "You've added a martial art, thank you!"})
        return render(request, self.template_name, {'form': form})


class AddTechniqueTypeView(View):
    template_name = 'add_technique_type.html'

    def get(self, request):
        form = TechniqueTypeForm()
        martial_arts = MartialArt.objects.all()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TechniqueTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'message': "You've added a technique type, thank you!"})
        martial_arts = MartialArt.objects.all()
        return render(request, self.template_name, {'form': form})