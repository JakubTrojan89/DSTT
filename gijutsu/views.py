from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from gijutsu.forms import MartialArtForm, TechniqueTypeForm, TechniqueForm, BeltColorForm, BeltRankingForm, \
    MartialArtSearchForm, TechniqueSearchForm
from gijutsu.models import MartialArt, Technique, TechniqueType


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


class ListMartialArtView(ListView):
    def get(self, request):
        martial_arts = MartialArt.objects.all()
        form = MartialArtSearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            martial_arts = martial_arts.filter(name__icontains=name)

        return render(request, 'list_view.html', {'object_list': martial_arts, 'form': form})


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

class ListTechniqueTypeView(ListView):

    def get(self, request):
        techniquetype = TechniqueType.objects.all()
        return render(request, 'list_view.html', {'object_list': techniquetype})


class AddTechniqueView(View):
    template_name = 'add_technique.html'

    def get(self, request):
        form = TechniqueForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TechniqueForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.template_name, {'message': "You've added a technique"})
        return render(request, self.template_name, {'form': form})


class ListTechniqueView(ListView):
    model = Technique
    template_name = 'list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = TechniqueSearchForm
        return context


class AddBeltColorView(View):
    template_name = 'add_belt_color.html'

    def get(self, request):
        form = BeltColorForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BeltColorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_belt_color.html', {'message': "You've added a belt color, thank you!"})
        return render(request, self.template_name, {'form': form})


class AddBeltRankingView(View):
    template_name = 'add_belt_ranking.html'

    def get(self, request):
        form = BeltRankingForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BeltRankingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_belt_ranking.html', {'message': "You've added a belt ranking, thank you!"})
        return render(request, self.template_name, {'form': form})