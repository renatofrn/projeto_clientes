from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome'] # http://localhost:8000/clientes/?ordering=nome
    search_fields = ['nome', 'cpf'] # http://localhost:8000/clientes/?search=Ana
    filterset_fields = ['ativo'] #http://localhost:8000/clientes/?ativo=true&search=Ana&ordering=-nome

