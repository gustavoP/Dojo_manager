from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
#from django.core.validators import DecimalField
from datetime import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
    		message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],
    	 max_length=17, 
    	 blank=False) # validators should be a list
    observacoes = models.TextField(blank=True)
    #    author = models.ForeignKey('auth.User')

    def change_phone(self,new_phone):
        self.phone_number = new_phone
        self.save()

    def __str__(self):
        return self.nome

class Modalidade(models.Model):
	nome = models.CharField(max_length=50, blank=False)
	dias = models.TextField(blank=False)

	def __str__(self):
		return self.nome

class Aluno(models.Model):
    pessoa = models.ForeignKey(Pessoa, 
    	on_delete=models.CASCADE, 
    	related_name='pessoa', 
    	blank=False)
    slug_name = models.CharField(max_length=30,blank=True)
    birth_date = models.DateTimeField(default=datetime.now, blank=False)
    responsavel = models.ForeignKey(Pessoa, 
    	on_delete=models.CASCADE, 
    	related_name='responsavel',
    	blank=True, 
    	null=True)
    #include list of modalidades
    modalidade = models.ForeignKey(Modalidade, 
    	on_delete=models.CASCADE, 
    	blank=False,
    	null=True)

    def change_responsavel(self,novo_responsavel):
        self.responsavel = pessoa;
        self.save()

    def __str__(self):
        return self.pessoa.__str__()



class Transacoes(models.Model):
	DINHEIRO = 'Dinheiro'
	DEPOSITO = 'Deposito'
	TRANSFERENCIA = 'Transferência'
	CHEQUE = 'Cheque'
	OUTRO = 'Outros' 

	FORMAS_PAGAMENTOS = (
    	(None, 'Escolha a forma de pagamento realizada'),
    	(DINHEIRO, 'Dinheiro'),
    	(DEPOSITO, 'Deposito'),
    	(TRANSFERENCIA, 'Trasferência bancária'),
    	(CHEQUE, 'Cheque'),
    	(OUTRO, 'Outros - Especificar')
	)

	pessoa = models.ForeignKey(
		Pessoa, 
		on_delete=models.CASCADE, 
		blank=False)
	data = models.DateTimeField(default=datetime.now, blank=False)
	valor = models.DecimalField(
		max_digits=8,
		decimal_places=2,
		blank=False)
		#validators=[DecimalValidator(max_decimal_places=2, max_whole_places=6)], 
	forma_pagamento = models.CharField(max_length=20, choices=FORMAS_PAGAMENTOS)
	pagamento_referente_a = models.TextField(blank=False, 
		help_text='Colocar quais meses o pagamento é referente especificando o ano também')
	

	def __str___(self):
		return self.pessoa.__str__() + ' ' +str(self.data)+ ' ' + str(self.valor)