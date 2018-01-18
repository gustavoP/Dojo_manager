from django.shortcuts import render

# Create your views here.
def pagina_aluno(request, inscricao):
    return render(request, 'aluno.html', {})