from django.shortcuts import render
from.forms import PatientForm
# Create your views here.
#test
def index(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            pass #on ne fait rien pour l'instant
    else:
        form = PatientForm()

    return render(request, "index.html", {'form':form})

def prediction(request):
    return render(request, "prediction.html")
