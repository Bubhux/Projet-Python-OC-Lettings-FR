import logging

from sentry_sdk import capture_exception
from django.shortcuts import render

from .models import Letting


# Initialisation du logger
logger = logging.getLogger(__name__)


def index(request):
    """
    Affiche une liste de toutes les locations disponibles.
    :param request: La requête HTTP reçue du navigateur
    :return: Une page HTML affichant la liste des locations
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.exception("Erreur dans la fonction index : %s", str(e))
        return render(request, 'error.html')


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique en fonction de son ID.
    :param request: La requête HTTP reçue du navigateur
    :param letting_id: L'ID de la location à afficher
    :return: Une page HTML affichant les détails de la location
    """
    try:
        if str(letting_id).isdigit():
            if Letting.objects.filter(id=letting_id):
                letting = Letting.objects.get(id=letting_id)
                context = {
                    'title': letting.title,
                    'address': letting.address,
                }
                return render(request, 'lettings/letting.html', context)
            else:
                capture_exception(Exception("Invalid ID"))
                return render(
                    request,
                    'oc_lettings_site/error_template.html', {'error_code': 500}, status=500
                )
        else:
            capture_exception(TypeError("Type error invalid ID"))
            return render(
                request,
                'oc_lettings_site/error_template.html', {'error_code': 500}, status=500
            )
    except Exception as e:
        logger.error("Erreur dans la fonction letting : %s", str(e))
        capture_exception(e)


def server_error(request):
    """
    Gère les erreurs 500 (page server_error) et envoie une alerte à Sentry.
    :param request: La requête HTTP reçue du navigateur
    :return: Une page HTML pour l'erreur 500
    """
    logger.error("Erreur 500")
    capture_exception()

    return render(request, 'oc_lettings_site/error_template.html', {'error_code': 500}, status=500)


def test_404(request):
    """
    Fonction de test pour générer une erreur 404 personnalisée.
    Et envoie une alerte à Sentry.
    :param request: La requête HTTP reçue du navigateur
    :return: Une page HTML pour l'erreur 404
    """
    logger.error("Erreur 404")
    capture_exception()
    return render(request, 'oc_lettings_site/error_template.html', {'error_code': 404}, status=404)
