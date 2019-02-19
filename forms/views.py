from django.http import HttpResponse
import django.http
import random, string

from .models import TableA, TableB
from django.template import loader

def index(request):
    return HttpResponse("Главная страница форм")

def printB(request):
    data = TableB.objects.all()
    tmp = loader.get_template("forms/tableB.html")
    context = {
        'data': data,
    }
    return HttpResponse(tmp.render(context, request))


def copyTableAtoB(request):
    data = TableA.objects.all()
    TableB.objects.all().delete()
    if (data):
        for l in data:
            hasher = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
            newLine = TableB(bPersonName = l.aPersonName, bPersonSurname = l.aPersonSurname, generatedPassWord = hasher  )
            newLine.save()
        return HttpResponse("Копирование выполнено успешно")
    else:
        return HttpResponse("Таблица А пуста. Нечего копировать")

def copyButton(request):
    tmp = loader.get_template("forms/copyBut.html")
    return HttpResponse(tmp.render({}, request))

def addA(request):
    tmp = loader.get_template("forms/formA.html")
    return HttpResponse(tmp.render({}, request))

def processFormA(request):
    newLine = TableA(aPersonName = request.POST['name'], aPersonSurname = request.POST['surname'])
    newLine.save()
    return HttpResponse("OK")
