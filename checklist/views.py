from django.shortcuts import render
from .models import Step, Checklist


def itinerary(request):
    """
    Create an introductory page for Django preflight planner. 
    
    """
    items = Checklist.objects.order_by("ordering")     # queryset
    context = {'items': items}

    return render(request, 'django_preflight.html', context)


# def checked(request, pk=True):
#     """
#     Creates a new Ice Cream record in the database
#     from the url.
#
#     A view is a function that takes an HTTP request
#     and returns an HTTP response.
#
#     """
#     item_checked = ListItem.objects.get(pk=pk)
#     context = {'item_checked': item_checked}
#
#     return render(request, 'django_preflight.html', context)