from django.contrib import admin
from .models import Pessoa
from .models import Aluno
from .models import Modalidade
from .models import Transacoes
# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Aluno)
admin.site.register(Modalidade)
admin.site.register(Transacoes)