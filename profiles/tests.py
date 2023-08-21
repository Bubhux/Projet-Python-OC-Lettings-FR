from django.test import TestCase, Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed
import pytest

from .models import Profile, User


class TestProfilesApp(TestCase):
    """Classe de tests pour les vues, les URLs et les modèles de l'application "profiles"."""
    client = Client()

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Test City'
        )
        # Variables pour stocker les chemins d'URL et les instances d'objets dans la méthode setUp
        self.path_index = reverse('profiles:index')
        self.path_profile = reverse('profiles:profile', kwargs={'username': self.user.username})

    @pytest.mark.django_db
    def test_profiles_index_view(self):
        """Vérifie que la vue d'index des profils renvoie un statut 200,
           que le contenu de la réponse contient le nom d'utilisateur du profil
           et que le bon modèle de template est utilisé.
        """
        response = self.client.get(self.path_index)
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile.user.username, content)
        assertTemplateUsed(response, 'profiles/index.html')

    @pytest.mark.django_db
    def test_profile_detail_view(self):
        """Vérifie que la vue de détail d'un profil renvoie un statut 200,
           que le contenu de la réponse contient le nom d'utilisateur du profil
           et que le bon modèle de template est utilisé.
        """
        response = self.client.get(self.path_profile)
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.profile.user.username, content)
        assertTemplateUsed(response, 'profiles/profile.html')

    @pytest.mark.django_db
    def test_profiles_index_url(self):
        """Vérifie que l'URL de l'index des profils est correcte
           et que la résolution de l'URL renvoie le bon nom de vue.
        """
        self.assertEqual(self.path_index, '/profiles/')
        self.assertEqual(resolve(self.path_index).view_name, 'profiles:index')

    @pytest.mark.django_db
    def test_profile_detail_url(self):
        """Vérifie que l'URL de détail d'un profil est correcte,
           et que la résolution de l'URL renvoie le bon nom de vue.
        """
        self.assertEqual(self.path_profile, f'/profiles/{self.user.username}/')
        self.assertEqual(resolve(self.path_profile).view_name, 'profiles:profile')

    @pytest.mark.django_db
    def test_user_model(self):
        """Vérifie que la représentation sous forme de chaîne de caractères
           de l'objet User est correcte.
        """
        user = User.objects.get(username=self.user.username)
        expected_value = self.user.username
        self.assertEqual(str(user), expected_value)

    @pytest.mark.django_db
    def test_profile_model(self):
        """Vérifie que la représentation sous forme de chaîne de caractères
           de l'objet Profile est correcte.
        """
        profile = Profile.objects.get(favorite_city=self.profile.favorite_city)
        expected_value = str(self.profile)
        self.assertEqual(str(profile), expected_value)
