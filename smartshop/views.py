from django.shortcuts import get_object_or_404, render

from smartshop.models import Category, Product

# Create your views here.
def ProductList(request):
    products = Product.objects.all()
    products = products.order_by('-publish')
    categories = Category.objects.filter(parent__isnull=True)
    context = {
        'products':products,
        'categories':categories,
    }
    template = 'products/product_list.html'
    return render(request, template ,context)


def products_by_category(request,category_slug):
    products = Product.objects.all()
    categories = Category.objects.filter(parent__isnull=True)
    slug = category_slug
    if slug:
        category_s = get_object_or_404(Category,slug = slug)    
        products = products.filter(category = category_s)
    context = {
        'products':products,
        'categories':categories,
        'category':category_s,
        'page_obj':page_obj,
    }
    template = 'products/products_by_category_list.html'
    return render(request,template,context)