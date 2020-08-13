from django.shortcuts import render


def index(request):
    return render(request, 'Dashboard/i-dashboard.html', context=None)
