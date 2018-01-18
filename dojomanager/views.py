from django.shortcuts import render
from .models import Aluno
from .models import Transacoes
from .models import Pessoa

# Create your views here.
def pagina_aluno(request, inscricao):
	aluno = Aluno.objects.get(id=inscricao)
	transacoes = Transacoes.objects.filter(pessoa=aluno.pessoa)
    
	return render(request, 'aluno.html', {'transacoes': transacoes, 'aluno': aluno})