from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'base.html')

# Til að sjá ekki ef ekki loggaður inn
# @login_required
# def blabla():
# pass
