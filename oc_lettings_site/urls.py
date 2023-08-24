from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.http import HttpResponseServerError
from sentry_sdk import capture_exception


from .views import index, server_error_500, custom_404


def trigger_error(request):
    """
    Fonction de test Sentry
    """
    try:
        division_by_zero = 1 / 0
        print(division_by_zero)
    except Exception as e:
        capture_exception(e)
        error_message = (
            f"Une erreur s'est produite lors du déclenchement de l'exception : "
            f"{str(e)}"
        )
        return HttpResponseServerError(error_message)


urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', index, name='index'),
    path(r'lettings/', include('lettings.urls', namespace='lettings')),
    path(r'profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    url(r'^404/$', custom_404),
    url(r'^500/$', server_error_500),

    # Utiliser le gestionnaire 404 par défaut pour le reste des cas
    url(r'^.*$', custom_404)
]
