from django.contrib import admin # type: ignore
from .models import Pessoa, Diario

admin.site.register(Pessoa)
admin.site.register(Diario)