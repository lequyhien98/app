from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Brand, Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def navigation(request):
    brand_list = Brand.objects.all()
    context = {
        'brand_list': brand_list,
    }
    return context

def Home(request):
    product_list = Product.objects.all().order_by('-created_at')

    context = {
        'product_list': product_list,
    }

    return render(request, 'app/home.html', context)


def Detail(request, id):
    product_item = Product.objects.get(id=id)
    product_list = Product.objects.all()

    context = {
        'product_item': product_item,
        'product_list': product_list,
    }

    return render(request, 'app/detail.html', context)


class ProductCreate(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'picture', 'brand']

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'price', 'description', 'picture', 'brand']

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ProductDelete(DeleteView):

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Product, id=id_)

    def get_success_url(self):
        return reverse('app:home')
