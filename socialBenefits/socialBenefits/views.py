from django.http import HttpResponse

def current_datetime(request):
    return HttpResponse("<html><body>.</body></html>")