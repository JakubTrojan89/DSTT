from django.urls import path
from gijutsu import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name='main'),
    path('martialart/', views.MartialArtView.as_view(), name='martial_art'),
    path('listmartialart/', views.ListMartialArtView.as_view(), name='list_martial_art'),
    path('addmartialart/', views.AddMartialArtView.as_view(), name='add_martial_art'),
    path('addtechniquetype/', views.AddTechniqueTypeView.as_view(), name='att'),
    path('listtechniquetype/', views.ListTechniqueTypeView.as_view(), name='list_technique_type'),
    path('addtechnique/', views.AddTechniqueView.as_view(), name='add_technique'),
    path('listtechnique/', views.ListTechniqueView.as_view(), name='list_technique'),
    path('detailtechnique/<int:pk>', views.DetailTechniqueView.as_view(), name='detail_technique'),
    path('addbeltranking/', views.AddBeltRankingView.as_view(), name='add_belt_ranking'),
    path('listbeltranking/', views.ListBeltRankingView.as_view(), name='list_belt_ranking'),
    path('addbeltcolor/', views.AddBeltColorView.as_view(), name='add_belt_color'),
    path('bjj/', views.BJJView.as_view(), name='bjj'),
    path('judo/', views.JudoView.as_view(), name='judo'),
    path('wrestling/', views.WrestlingView.as_view(), name='wrestling'),
    path('submission/', views.SubmissionView.as_view(), name='submission_grappling'),
]