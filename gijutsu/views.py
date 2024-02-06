from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import ListView, UpdateView

from gijutsu.forms import MartialArtForm, TechniqueTypeForm, TechniqueForm, BeltColorForm, BeltRankingForm, \
    MartialArtSearchForm, TechniqueSearchForm, MartialArtLegendForm, AddCommentForm
from gijutsu.models import MartialArt, Technique, TechniqueType, Comment, MartialArtLegends


class MainPageView(View):
    def get(self, request):
        return render(request, 'index.html')


class MartialArtView(View):
    def get(self, request):
        martial_art = ['BJJ', 'Submission Grappling', 'Wrestling', 'Judo']
        return render(request, 'martial_art.html', {'martial_art': martial_art})


class AddMartialArtView(LoginRequiredMixin, View):
    template_name = 'add_martial_art.html'

    def get(self, request):
        form = MartialArtForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MartialArtForm(request.POST)
        if form.is_valid():
            form.save()
            message = "You've added a martial art, thanks!"
            return render(request, self.template_name, {'message': message})
        return render(request, self.template_name, {'form': form})


class ListMartialArtView(View):
    def get(self, request):
        martial_arts = MartialArt.objects.all()
        form = MartialArtSearchForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get('name', '')
            martial_arts = martial_arts.filter(name__icontains=name)

        return render(request, 'list_view.html', {'object_list': martial_arts, 'form': form})


class AddTechniqueTypeView(LoginRequiredMixin, View):
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


class ListTechniqueTypeView(View):

    def get(self, request):
        techniquetype = TechniqueType.objects.all()
        return render(request, 'list_view.html', {'object_list': techniquetype})


class AddTechniqueView(View):
    template_name = 'add_technique.html'

    def get(self, request):
        form = TechniqueForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TechniqueForm(request.POST)
        if form.is_valid():
            martial_art = form.cleaned_data['martial_art']
            technique = form.save()
            technique.martial_art.set(martial_art)
            return redirect('add_technique')
        return render(request, self.template_name, {'form': form})


class ListTechniqueView(View):
    template_name = 'list_technique_view.html'

    def get(self, request):
        form = TechniqueSearchForm(request.GET)
        techniques = Technique.objects.all()

        if form.is_valid():
            name = form.cleaned_data['title']

            if name:
                techniques = techniques.filter(name__icontains=name)

        context = {'form': form, 'techniques': techniques}
        return render(request, self.template_name, context)


class DetailTechniqueView(View):

    def get(self, request, pk):
        try:
            technique = Technique.objects.get(pk=pk)
        except Technique.DoesNotExist:
            raise Http404("Technique does not exist")

        # Przekazujemy technikę do szablonu HTML
        return render(request, 'technique_detail.html', {'technique': technique})


class AddBeltColorView(LoginRequiredMixin, View):
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


class AddMartialArtLegendView(View):
    template_name = 'add_martial_art_legend.html'

    def get(self, request):
        form = MartialArtLegendForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MartialArtLegendForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'add_martial_art_legend.html')
        return render(request, self.template_name, {'form': form})


class ListMartialArtLegendView(View):
    template_name = 'list_martial_art_legends.html'

    def get(self, request):
        legends = MartialArtLegends.objects.all()
        return render(request, self.template_name, {'legends': legends})


class AddCommentView(View):

    def get(self, request, technique_pk):
        form = AddCommentForm()
        return render(request, 'add_technique.html', {'form': form})

    def post(self, request, technique_pk):
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.technique = Technique.objects.get(pk=technique_pk)
            comment.martial_art = self.request.user
            comment.save()
            return redirect('detail_book', args=(technique_pk, ))
        return render(request, 'add_technique.html', {'form': form})


class EditCommentView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

    model = Comment
    fields = ['text']
    template_name = 'add_form.html'

    def get_success_url(self):
        return reverse('detail_technique', args=(self.object.technique.pk))


class BJJView(View):
    def get(self, request):
        return render(request, 'bjj.html')


class JudoView(View):
    def get(self, request):
        return render(request, 'judo.html')


class WrestlingView(View):
    def get(self, request):
        return render(request, 'wrestling.html')


class SubmissionView(View):
    def get(self, request):
        return render(request, 'submission.html')


# def user_panel(request):
#     return render(request, 'user_panel.html')

