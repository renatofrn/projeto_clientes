# -*- coding: utf-8 -*-
from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    # FORMA 2 DE VALIDAÇÃO: usando validators para armazenar as funções de verificação
    def validate(self, data):
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo."})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "Número de CPF inválido."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': 'O RG deve ter exatamente 9 dígitos numéricos.'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': "O celular deve seguir o padrão 62 91234-1234 respeitando espaço e traço."})
        return data
    # FORMA 2 DE VALIDAÇÃO:

    # FORMA 1 DE VALIDAÇÃO:
    # def validate_cpf(self, cpf):
    #     if cpf.isalpha():
    #         raise serializers.ValidationError("Não inclua letras neste campo.")
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
    #     return cpf
    #
    # def validate_rg(self, rg):
    #     if rg.isalpha():
    #         raise serializers.ValidationError("Não inclua letras neste campo.")
    #     if len(rg) != 9:
    #         raise serializers.ValidationError("O RG deve ter 9 dígitos")
    #     return rg
    #
    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("Não inclua números neste campo")
    #     return nome
    #
    # def validate_celular(self, celular):
    #     if celular.isalpha():
    #         raise serializers.ValidationError("Não inclua letras neste campo.")
    #     if len(celular) < 11:
    #         raise serializers.ValidationError("O celular deve ter pelo menos 11 dígitos.")
    #     return celular
    # FORMA 1 DE VALIDAÇÃO:


