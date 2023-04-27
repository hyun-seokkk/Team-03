from django.shortcuts import render, redirect
from .models import Dining
from .forms import DiningForm

# Create your views here.
def index(request):
    pass


def dining_create(request):
    if request.method == 'POST':
        form = DiningForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dinings:index')
            
    else:
        form = DiningForm()
    context = {
        'form': form,
    }
    return render(request, 'dinings/dining_create.html', context)