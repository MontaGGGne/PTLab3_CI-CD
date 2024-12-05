import math
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

DECREASE = 10

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'product_quantity', 'person', 'address']

    def form_valid(self, form):
        self.object = form.save()
        product_quantity = self.object.product_quantity
        print(f"product_quantity - {product_quantity}")
        product_id = self.object.product_id
        print(f"product_id - {product_id}")
        try:
            product = Product.objects.filter(id=product_id).first()
        except Exception as e:
            print(repr(e))
            exit(0)

        print(f"product - {product}")
        try:
            pq = product.quantity
        except Exception as e:
            print(repr(e))
            exit(0)

        # all_sum = 0
        # counter = 0
        # round_p_q = int(math.ceil(product.quantity))
        # p_diff = round_p_q - product.quantity
        # while product_quantity > 0:
        #     if product_quantity <= p_diff:
        #         all_sum += product_quantity * product.price
        #         product_quantity -= product_quantity
        #     elif counter == 0:
        #         product_quantity -= p_diff
        #         all_sum += p_diff * product.price
        #         product.quantity = product.quantity - p_diff
        #         p_diff = 
        #     else:
        #         product.quantity = product.quantity - product_quantity

        print(f"product.quantity before - {product.quantity}")
        product.quantity = product.quantity - product_quantity
        print(f"product.quantity - {product.quantity}")
        
        coeff_quantity = int(math.floor((product.max_quantity - product.quantity)/10))
        percent_coeff = int(product.growth_percentage/15)
        if coeff_quantity > percent_coeff:
            product.growth_percentage += (coeff_quantity - percent_coeff) * 15
            
        product.price += (product.price * product.growth_percentage)/100
        
        product.save()
        return HttpResponse(f'Спасибо за покупку, {self.object.person}!')

