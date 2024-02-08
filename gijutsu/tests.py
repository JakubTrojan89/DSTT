import pytest
from django.test import TestCase
from django.urls import reverse

from gijutsu.models import MartialArt, Technique, TechniqueType, BeltColor, BeltRanking, MartialArtLegends


class MartialArtModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MartialArt.objects.create(name='Karate', description='Japanese martial art.')

    def test_name_content(self):
        martial_art = MartialArt.objects.get(id=1)
        expected_object_name = martial_art.name
        self.assertEquals(expected_object_name, 'Karate')

    def test_description_content(self):
        martial_art = MartialArt.objects.get(id=1)
        expected_object_description = martial_art.description
        self.assertEquals(expected_object_description, 'Japanese martial art.')


class TechniqueTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        TechniqueType.objects.create(name='Striking', description='Focuses on powerful blows.')

    def test_name_content(self):
        technique_type = TechniqueType.objects.get(id=1)
        expected_object_name = technique_type.name
        self.assertEquals(expected_object_name, 'Striking')

    def test_description_content(self):
        technique_type = TechniqueType.objects.get(id=1)
        expected_object_description = technique_type.description
        self.assertEquals(expected_object_description, 'Focuses on powerful blows.')


class TechniqueModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        martial_art = MartialArt.objects.create(name='Karate', description='Japanese martial art.')
        technique_type = TechniqueType.objects.create(name='Striking', description='Focuses on powerful blows.')
        Technique.objects.create(name='Punch', description='Straight punch technique.', martial_art=martial_art, technique_type=technique_type)

    def test_name_content(self):
        technique = Technique.objects.get(id=1)
        expected_object_name = technique.name
        self.assertEquals(expected_object_name, 'Punch')

    def test_description_content(self):
        technique = Technique.objects.get(id=1)
        expected_object_description = technique.description
        self.assertEquals(expected_object_description, 'Straight punch technique.')

    def test_martial_art_relation(self):
        technique = Technique.objects.get(id=1)
        related_martial_art = technique.martial_art.first()
        self.assertEquals(related_martial_art.name, 'Karate')

    def test_technique_type_relation(self):
        technique = Technique.objects.get(id=1)
        related_technique_type = technique.technique_type
        self.assertEquals(related_technique_type.name, 'Striking')


class BeltColorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        martial_art = MartialArt.objects.create(name='Karate', description='Japanese martial art.')
        BeltColor.objects.create(color_name='Black', martial_art=martial_art)

    def test_color_name_content(self):
        belt_color = BeltColor.objects.get(id=1)
        expected_color_name = belt_color.color_name
        self.assertEquals(expected_color_name, 'Black')

    def test_martial_art_relation(self):
        belt_color = BeltColor.objects.get(id=1)
        related_martial_art = belt_color.martial_art
        self.assertEquals(related_martial_art.name, 'Karate')


class BeltRankingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        martial_art = MartialArt.objects.create(name='Karate', description='Japanese martial art.')
        BeltRanking.objects.create(belt_color='Black', martial_art=martial_art)

    def test_belt_color_content(self):
        belt_ranking = BeltRanking.objects.get(id=1)
        expected_belt_color = belt_ranking.belt_color
        self.assertEquals(expected_belt_color, 'Black')

    class MartialArtLegendsModelTest(TestCase):
        @classmethod
        def setUpTestData(cls):
            martial_art = MartialArt.objects.create(name='Karate', description='Japanese martial art.')
            MartialArtLegends.objects.create(first_name='Bruce', last_name='Lee', martial_art=martial_art)

        def test_full_name_content(self):
            martial_art_legend = MartialArtLegends.objects.get(id=1)
            expected_full_name = f'{martial_art_legend.first_name} {martial_art_legend.last_name}'
            self.assertEquals(expected_full_name, 'Bruce Lee')

        def test_martial_art_relation(self):
            martial_art_legend = MartialArtLegends.objects.get(id=1)
            related_martial_art = martial_art_legend.martial_art
            self.assertEquals(related_martial_art.name, 'Karate')


class BJJViewTest(TestCase):
    def test_bjj_view(self):
        response = self.client.get(reverse('bjj'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bjj.html')


class JudoViewTest(TestCase):
    def test_judo_view(self):
        response = self.client.get(reverse('judo'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'judo.html')


class WrestlingViewTest(TestCase):
    def test_wrestling_view(self):
        response = self.client.get(reverse('wrestling'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wrestling.html')


class SubmissionViewTest(TestCase):
    def test_submission_view(self):
        response = self.client.get(reverse('submission'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submission.html')


