from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Minun oma sivuni")

def laske_summa(request):
    
    sivun_vastaus = 54 + 23

    return HttpResponse(sivun_vastaus)