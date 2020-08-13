from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    # current_user = User.objects.get(id=request.)
    # print(current_user.position)
    print(request.user.user_position)
    return render(request, 'Dashboard/i-dashboard.html', context=None)
