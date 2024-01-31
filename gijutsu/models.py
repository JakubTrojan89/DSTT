from django.db import models


class MartialArt(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.name


class TechniqueType(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)

    def __str__(self):
        return self.name


class Technique(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    martial_art = models.ManyToManyField(MartialArt)
    technique_type = models.ForeignKey(TechniqueType, on_delete=models.CASCADE)

    def __str__(self):
        return self.technique_type


class BeltColor(models.Model):
    color_name = models.CharField(max_length=64)
    martial_art = models.ForeignKey(MartialArt, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.color_name} - {self.martial_art}'


class BeltRanking(models.Model):
    belt_color = models.CharField(max_length=64)
    martial_art = models.ForeignKey(MartialArt, on_delete=models.CASCADE)
    technique = models.ManyToManyField(Technique, related_name='belt_ranking')

    def __str__(self):
        return f'{self.belt_color} - {self.martial_art}'