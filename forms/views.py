from django.http import HttpResponse
import django.http
import random, string

from .models import TableA, TableB
from django.template import loader

def printB(request):
    data = TableB.objects.all()
    tmp = loader.get_template("forms/index.html")
    context = {
        'data': data,
    }
    return HttpResponse(tmp.render(context, request))


def copyTableAtoB(request):
    data = TableA.objects.all()
    if (data):
        for l in data:
            hasher = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
            newLine = TableB(bPersonName = l.aPersonName, bPersonSurname = l.aPersonSurname, generatedPassWord = hasher  )
            newLine.save()
        return HttpResponse("Копирование выполнено успешно")
    else:
        return HttpResponse("Таблица А пуста. Нечего копировать")
