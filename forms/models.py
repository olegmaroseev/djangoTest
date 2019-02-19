from django.db import models


class TableA(models.Model):
    aPersonName = models.CharField(max_length=200)
    aPersonSurname = models.CharField(max_length=200)

    def __str__(self):
        return self.aPersonName + " " + self.aPersonSurname


class TableB(models.Model):
    bPersonName = models.CharField(max_length=200)
    bPersonSurname = models.CharField(max_length=200)
    generatedPassWord = models.CharField(max_length=200)

    def __str__(self):
        return self.aPersonName + " " + self.bPersonSurname
