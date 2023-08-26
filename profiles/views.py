from django.shortcuts import render
from .models import Profile


def index(request):
    """
    Affiche la liste de tous les profils d'utilisateurs.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche le profil de l'utilisateur avec le nom d'utilisateur donné.
    Si le profil n'existe pas, affiche une page "not found".
    """
    if Profile.objects.filter(user__username=username):
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    else:
        return render(request, 'oc_lettings_site/error_template.html', {'error_code': 500}, status=500)
