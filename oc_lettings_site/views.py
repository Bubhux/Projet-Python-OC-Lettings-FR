from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def not_found_404(request, exception):
    return render(request, 'error_template.html', {'error_code': 404}, status=404)


def server_error_500(request):
    return render(request, 'error_template.html', {'error_code': 500}, status=500)


def custom_404(request):
    return render(request, 'error_template.html', {'error_code': 404}, status=404)
