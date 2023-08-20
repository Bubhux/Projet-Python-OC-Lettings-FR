from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def not_found(request):
    return render(request, 'not_found.html')


def trigger_error(request):
    """
    function to test sentry
    """
    division_by_zero = 1 / 0
    print(division_by_zero)
