from django.shortcuts import render


def index(request):
    return render(request, 'oc_lettings_site/index.html')


def server_error_500(request):
    return render(request, 'oc_lettings_site/error_template.html', {'error_code': 500}, status=500)


def custom_404(request):
    return render(request, 'oc_lettings_site/error_template.html', {'error_code': 404}, status=404)
