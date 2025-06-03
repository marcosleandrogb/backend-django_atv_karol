from django.views import generic
from django.urls import reverse_lazy
from .models import Cliente, Venda
from .forms import ClienteForm, VendaForm

# Cliente Views
class ClienteListView(generic.ListView):
    model = Cliente
    template_name = 'clientes/lista.html'

class ClienteCreateView(generic.CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteUpdateView(generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('cliente-list')

class ClienteDeleteView(generic.DeleteView):
    model = Cliente
    template_name = 'clientes/confirm_delete.html'
    success_url = reverse_lazy('cliente-list')

# Venda Views
class VendaListView(generic.ListView):
    model = Venda
    template_name = 'vendas/lista.html'
    context_object_name = 'vendas'

    def get_queryset(self):
        queryset = super().get_queryset()
        cliente = self.request.GET.get('cliente')
        data_inicio = self.request.GET.get('data_inicio')
        data_fim = self.request.GET.get('data_fim')

        if cliente:
            queryset = queryset.filter(cliente__nome__icontains=cliente)
        if data_inicio:
            queryset = queryset.filter(data_venda__gte=data_inicio)
        if data_fim:
            queryset = queryset.filter(data_venda__lte=data_fim)

        return queryset

class VendaCreateView(generic.CreateView):
    model = Venda
    form_class = VendaForm
    template_name = 'vendas/form.html'
    success_url = reverse_lazy('venda-list')