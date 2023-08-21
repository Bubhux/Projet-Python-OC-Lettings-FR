from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle pour stocker les informations de profil utilisateur.
    Chaque profil est associé à un utilisateur unique.
    """
    # L'utilisateur associé à ce profil. Le lien est en "one-to-one",
    # ce qui signifie qu'un profil est lié à un utilisateur unique.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # La ville préférée de l'utilisateur, pouvant être vide.
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne du profil.
        Par défaut, cela renvoie le nom d'utilisateur de l'utilisateur associé.
        """
        return self.user.username
