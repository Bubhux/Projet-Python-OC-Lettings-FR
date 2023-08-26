from django.urls import path
from django.conf.urls import url
from .views import index, letting, server_error, test_404


app_name = 'lettings'
urlpatterns = [
    path('', index, name='index'),
    path('<int:letting_id>/', letting, name='letting'),

    # Enregistre la vue server_error pour gérer les erreurs 500
    path('server_error/', server_error, name='server_error'),

    # Définis une vue qui génère intentionnellement une erreur 404
    # (à des fins de test)
    path('test_404/', test_404, name='test_404'),

    # Utilise la vue server_error par défaut pour le reste des cas
    url(r'^.*$', server_error),
]
