from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Welcome to demoproject")

def cource(request):
    return HttpResponse("Welcome to cources1")