from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Processo)
admin.site.register(Documento)
admin.site.register(Portaria)
admin.site.register(Pedido)
admin.site.register(Envio)
admin.site.register(Tranmitacoes)