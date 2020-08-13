from django.shortcuts import render
from django.contrib.auth import get_user_model

from Job.models import Jobs

User = get_user_model()


def index(request):
    # current_user = User.objects.get(id=request.)
    # print(current_user.position)
    jobs = Jobs.objects.all()

    if request.user.is_authenticated:
        current_user = request.user
        if current_user.user_position == 'HK':
            return render(request, 'Dashboard/hr-dashboard.html', context={'jobs': jobs})

        elif current_user.user_position == 'TL':
            return render(request, 'Dashboard/tl-dashboard.html', context={'jobs': jobs})

    return render(request, 'Dashboard/i-dashboard.html', context={'jobs': jobs})
