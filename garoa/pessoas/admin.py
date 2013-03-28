from django.contrib import admin

from .models import Pessoa, Contribuicao

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'celular', 'email', 'status')
    list_filter = ('status',)

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contribuicao)
