#importo las clasesd de Django
from django.http import HttpResponse

#Defino funcion que luego asocio con la url
def index(request):
    return HttpResponse('Hola Mundo!')