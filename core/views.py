from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home_view(request):
    return render(request, 'core/home.html')


@login_required
def dashboard_view(request):
    return render(request, 'core/dashboard.html',)
