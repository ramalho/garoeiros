from django.db import models

STATUS_CHOICES = [
    ('visitante', 'visitante'),
    ('padawan', 'padawan'),
    ('associado', 'associado'),
]

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.EmailField('e-mail', max_length=128)
    status = models.CharField(max_length=16,
                              choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0])
    celular = models.CharField('celular', max_length=32, blank=True,
            help_text='informar DDD')
    cpf = models.CharField('CPF', max_length=16, blank=True)
    nome_real = models.CharField('Nome legal', max_length=128, blank=True,
        help_text='nome completo como aparece no RG, RNE, passaporte...')

    def __str__(self):
        return self.nome

CONTRIBUICAO_CHOICES = [
    ('doacao', 'doação'),
    ('mensalidade', 'mensalidade'),
    ('anuidade', 'anuidade'),
]

class Contribuicao(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    tipo = models.CharField(max_length=16,
                            choices=CONTRIBUICAO_CHOICES,
                            default=CONTRIBUICAO_CHOICES[0][0])
    datahora_pagamento = models.DateTimeField()
    vigencia_inicio = models.DateField('Vigência (a partir de)', null=True)
    vigencia_termino = models.DateField('Vigência (até)', null=True)
    valor = models.DecimalField('Valor (R$)', max_digits=16,
                                              decimal_places=2)

    class Meta:
        verbose_name = 'contribuição'
        verbose_name_plural = 'contribuições'
