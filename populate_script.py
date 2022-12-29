# -*- coding: utf-8 -*-
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clientes.models import Cliente

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    cont = 1
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name().upper()
        # email = '{}@{}'.format(nome.lower(), fake.free_email_domain())
        email = '{}{}@{}'.format(nome.replace(" ", "")[0:10].lower(), random.randrange(1, 99), fake.free_email_domain())
        email = email.replace(' ', '')
        cpf = cpf.generate()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))
        celular = "{} 9{}-{}".format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        ativo = random.choice([True, False])
        print('({}) USUARIO CRIADO: {} | {} | {} | {} | {} | {}'.format(cont, nome, email, cpf, rg, celular, ativo))
        p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
        p.save()
        cont+=1

criando_pessoas(50)
print('Sucesso!')