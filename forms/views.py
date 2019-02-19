from django.http import HttpResponse
import django.http
import random, string

from .models import TableA, TableB
from django.template import loader

def index(request):
    data = TableA.objects.all()
    tmp = loader.get_template("forms/index.html")
    context = {
        'data': data,
    }
    return HttpResponse(tmp.render(context, request))


def copyTableAtoB(request):
    for l in TableA.objects.all():
        hasher = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
        newLine = TableB(bPersonName = l.aPersonName, bPersonSurname = l.aPersonSurname, generatedPassWord = hasher  )
        newLine.save()
    return HttpResponse("Копирование выполнено успешно")
