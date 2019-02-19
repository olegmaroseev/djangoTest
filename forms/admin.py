from django.contrib import admin

from .models import TableA
from .models import TableB

admin.site.register(TableA)
admin.site.register(TableB)
