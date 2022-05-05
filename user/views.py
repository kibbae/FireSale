from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


#user = [
#    {'name': 'Kristbjörg', 'kristbjorge21@ru.is'}
#]

# Create your views here.
def index(request):
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })