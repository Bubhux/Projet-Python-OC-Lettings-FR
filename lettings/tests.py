from django.test import TestCase, Client
from django.urls import reverse, resolve
from pytest_django.asserts import assertTemplateUsed
import pytest

from .models import Letting, Address


class TestLettingsApp(TestCase):
    """Classe de tests pour les vues, les URLs et les modèles de l'application "lettings"."""
    client = Client()

    def setUp(self):
        self.address = Address.objects.create(
            number=10,
            street="street",
            city="Konoha",
            state="Awaji",
            zip_code=86903,
            country_iso_code="JAP"
        )
        self.letting = Letting.objects.create(
            title="Konoha Pays du feu",
            address=self.address
        )
        # Variables pour stocker les chemins d'URL et les instances d'objets dans la méthode setUp
        self.path_index = reverse('lettings:index')
        self.path_letting = reverse('lettings:letting', kwargs={'letting_id': self.letting.id})

    @pytest.mark.django_db
    def test_lettings_index_view(self):
        """Vérifie que la vue d'index des lettings renvoie un statut 200,
           que le contenu de la réponse contient le titre de la première letting
           et que le bon modèle de template est utilisé.
        """
        response = self.client.get(self.path_index)
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting.title, content)
        assertTemplateUsed(response, 'lettings/index.html')

    @pytest.mark.django_db
    def test_letting_detail_view(self):
        """Vérifie que la vue de détail d'une letting renvoie un statut 200,
           que le contenu de la réponse contient le titre de la letting
           et que le bon modèle de template est utilisé.
        """
        response = self.client.get(self.path_letting)
        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.letting.title, content)
        assertTemplateUsed(response, 'lettings/letting.html')

    @pytest.mark.django_db
    def test_lettings_index_url(self):
        """ Vérifie que l'URL de l'index des lettings est correcte
            et que la résolution de l'URL renvoie le bon nom de vue.
        """
        self.assertEqual(self.path_index, '/lettings/')
        self.assertEqual(resolve(self.path_index).view_name, 'lettings:index')

    @pytest.mark.django_db
    def test_letting_detail_url(self):
        """Vérifie que l'URL de détail d'une letting est correcte,
           et que la résolution de l'URL renvoie le bon nom de vue.
        """
        self.assertEqual(self.path_letting, f'/lettings/{self.letting.id}/')
        self.assertEqual(resolve(self.path_letting).view_name, 'lettings:letting')

    @pytest.mark.django_db
    def test_address_model(self):
        """Vérifie que la représentation
           sous forme de chaîne de caractères de l'objet Address est correcte.
        """
        address = Address.objects.get(city=self.address.city)
        expected_value = str(self.address)
        self.assertEqual(str(address), expected_value)

    @pytest.mark.django_db
    def test_letting_model(self):
        """ Vérifie que la représentation
            sous forme de chaîne de caractères de l'objet Letting est correcte.
        """
        letting = Letting.objects.get(title=self.letting.title)
        expected_value = self.letting.title
        self.assertEqual(str(letting), expected_value)
