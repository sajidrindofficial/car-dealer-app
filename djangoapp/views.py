from django.shortcuts import render

def get_dealerships(request):
    return render(request, 'djangoapp/index.html')
