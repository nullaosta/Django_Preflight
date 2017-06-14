from django.shortcuts import render
from .models import ListItem



def itinerary(request):
    """
    Create an introductory page for Django preflight planner. 
    
    """
    items = ListItem.objects.all()
    context = {'items': items}

    return render(request, 'django_preflight.html', context)