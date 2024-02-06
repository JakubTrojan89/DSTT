from django.contrib import admin
from django.urls import path, include
from gijutsu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPageView.as_view(), name='main'),
    path('accounts/', include('accounts.urls')),
    path('martialart/', views.MartialArtView.as_view(), name='martial_art'),
    path('listmartialart/', views.ListMartialArtView.as_view(), name='list_martial_art'),
    path('addmartialart/', views.AddMartialArtView.as_view(), name='add_martial_art'),
    path('addtechniquetype/', views.AddTechniqueTypeView.as_view(), name='att'),
    path('listtechniquetype/', views.ListTechniqueTypeView.as_view(), name='list_technique_type'),
    path('addtechnique/', views.AddTechniqueView.as_view(), name='add_technique'),
    path('listtechnique/', views.ListTechniqueView.as_view(), name='list_technique'),
    path('detailtechnique/<int:pk>', views.DetailTechniqueView.as_view(), name='detail_technique'),
    path('addbeltranking/', views.AddBeltRankingView.as_view(), name='add_belt_ranking'),
    path('addlegend/', views.AddMartialArtLegendView.as_view(), name='add_legend'),
    path('listlegend/', views.ListMartialArtLegendView.as_view(), name='list_legend'),
    path('addbeltcolor/', views.AddBeltColorView.as_view(), name='add_belt_color'),
    path('bjj/', views.BJJView.as_view(), name='bjj'),
    path('judo/', views.JudoView.as_view(), name='judo'),
    path('wrestling/', views.WrestlingView.as_view(), name='wrestling'),
    path('submission/', views.SubmissionView.as_view(), name='submission_grappling'),
    path('addcomment/<int:technique_pk>/', views.AddCommentView.as_view(), name='add_comment'),
    path('editcomment/<int:technique_pk>/', views.EditCommentView.as_view(), name='edit_comment'),
    # path('userpanel/', views.user_panel().as_view(), name='user_panel'),
]