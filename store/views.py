from django.shortcuts import render


# Create your views here.
def storeapp(request):

    return render(request, "templates/first.html")
