from django.shortcuts import render

#user = [
#    {'name': 'Kristbjörg', 'kristbjorge21@ru.is'}
#]

# Create your views here.
def index(request):
    return render(request, 'user/index.html')