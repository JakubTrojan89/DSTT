from django.contrib import admin

from gijutsu.models import Technique, TechniqueType, BeltColor, BeltRanking, MartialArt, MartialArtLegends, Comment

# Register your models here.

admin.site.register(Technique)
admin.site.register(TechniqueType)
admin.site.register(BeltColor)
admin.site.register(BeltRanking)
admin.site.register(MartialArt)
admin.site.register(MartialArtLegends)
admin.site.register(Comment)