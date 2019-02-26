from django.shortcuts import render
from itertools import product
from django.http import HttpResponse
from .models import Product
from django.views import generic


def product_list(request): 
        querysets = Product.objects.all() 
        return render(request, 'product_list.html', {'qs': querysets})

def index(request):
        return render(request, 'index.html')

class ProductListView(generic.ListView):
    model = Product
    template_name = 'product.html'
    #paginate_by = 2
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product_view.html'
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'

        return context
