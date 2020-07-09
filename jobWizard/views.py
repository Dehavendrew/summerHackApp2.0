from django.shortcuts import render
#import summerHackApp/jobWizardalgo
from jobWizard.algo import findMeAJOB

# Create your views here.
def home(request):
    return render(request, 'index.html')

def secretPage(request):

    job = findMeAJOB('Drew');

    context = {
        'name': ['Drew D', 'Katherine', 'Katherine','Adam','Netra','Selena','Shivika'],
        'location':"Accenture",
        'jobs': job,
    }

    return render(request, 'secretPage.html', context)
