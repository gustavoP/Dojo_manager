from django.shortcuts import render
from .models import Aluno
from .models import Transacoes
from .models import Pessoa

# Create your views here.
def pagina_aluno(request, inscricao):
	#aluno_nome='Gustavo Pacheco Epifanio'
	pessoa=Pessoa.objects.get(id=inscricao)

	aluno = Aluno.objects.get(pessoa=pessoa)
	transacoes = Transacoes.objects.filter(pessoa=pessoa)
    
	return render(request, 'aluno.html', {'transacoes': transacoes, 'aluno': aluno})