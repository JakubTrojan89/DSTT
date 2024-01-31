from django.db import models


class MartialArt(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=512)


class TechniqueType(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)


class Technique(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    martial_arts = models.ManyToManyField(MartialArt)
    technique_type = models.ForeignKey(TechniqueType, on_delete=models.CASCADE)


class BeltRanking(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    martial_arts = models.ForeignKey(MartialArt, on_delete=models.CASCADE)
    technique = models.ForeignKey(Technique, on_delete=models.DO_NOTHING)
