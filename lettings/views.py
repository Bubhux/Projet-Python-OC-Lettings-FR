from django.shortcuts import render
from .models import Letting


def index(request):
    """
    Affiche une liste de toutes les locations disponibles.
    :param request: La requête HTTP reçue du navigateur
    :return: Une page HTML affichant la liste des locations
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche les détails d'une location spécifique en fonction de son ID.
    :param request: La requête HTTP reçue du navigateur
    :param letting_id: L'ID de la location à afficher
    :return: Une page HTML affichant les détails de la location
    """
    if str(letting_id).isdigit():
        if Letting.objects.filter(id=letting_id):
            letting = Letting.objects.get(id=letting_id)
            context = {
                'title': letting.title,
                'address': letting.address,
            }
            return render(request, 'lettings/letting.html', context)
        else:
            return render(request, 'not_found.html')
    else:
        return render(request, 'not_found.html')
