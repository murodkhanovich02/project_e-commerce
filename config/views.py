from django.shortcuts import render
from django.views import View

from product.models import Category, Product


class LandingPageView(View):

    def get(self, request):
        category = Category.objects.all()
        latest_product = Product.objects.all().order_by('-created_at').first()
        other_product = Product.objects.all().order_by('-created_at')
        context = {
            'category': category,
            'latest_product': latest_product,
            'other_product': other_product,
        }
        return render(request, 'main.html', context)
