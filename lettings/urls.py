from django.urls import path
from django.conf.urls import url
from .views import index, letting, not_found, test_404
from oc_lettings_site.views import custom_404


app_name = 'lettings'
urlpatterns = [
    path('', index, name='index'),
    path('<int:letting_id>/', letting, name='letting'),

    # Enregistrez la vue not_found pour gérer les erreurs 404
    path('not_found/', not_found, name='not_found'),

    # Définissez une vue qui génère intentionnellement une erreur 404
    # (à des fins de test)
    path('test_404/', test_404, name='test_404'),

    # Utiliser le gestionnaire 404 par défaut pour le reste des cas
    url(r'^.*$', custom_404),
]
