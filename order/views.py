from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.utils.crypto import get_random_string

from User.models import UserProfile
from order.models import ShopCart, ShopCartForm, OrderForm, Order, OrderProduct, DeliveredPayment 
from shop.models import Category, Product
from order.forms import PaymentForm


# Create your views here.


def homeview(request):
    return HttpResponse("order page")

def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user 

    checkproduct = ShopCart.objects.filter(product_id=id)
    if checkproduct:
        control = 2
    else:
        control = 0

    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.color = form.cleaned_data['color']
                data.size = form.cleaned_data['size']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.color = form.cleaned_data['color']
                data.size = form.cleaned_data['size']
                data.save()
        messages.success(request, "product added to shopcart")
        return HttpResponseRedirect(url)

    else:
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "product added to shopcart")
        return HttpResponseRedirect(url)


def shoping_cart(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
             total += rs.product.discount_price * rs.quantity
    context = {'category': category,
               'shopcart': shopcart,
               'total': total
               }
    return render(request, "shopping-cart.html", context)


def delete_cart(request, id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, "Your item is deleted from Shopcart")
    return  HttpResponseRedirect('/shopingcart')


def orderproductviews(request):
    category = Category.objects.all()
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id=current_user.id)
    total = 0
    for rs in shopcart:
        total += rs.product.discount_price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.phone = form.cleaned_data['phone']
            data.region = form.cleaned_data['region']
            data.district = form.cleaned_data['district']
            data.street_address = form.cleaned_data['street_address']
            data.apartment_address = form.cleaned_data['apartment_address']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            shopcart = ShopCart.objects.filter(user_id=current_user.id)
            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                detail.color = rs.color
                detail.size = rs.size
                detail.price = rs.product.price
                detail.save()

            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] = 0
            messages.success(request, "Your Oder has been completed. Thank you")
            context = {'category': category,
                       'ordercode': ordercode
                       }
            return render(request, 'order_completed.html', context)
            #return redirect('/order/payment/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct/")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'shopcart': shopcart,
               'category': category,
               'total': total,
               'form': form,
               'profile': profile
               }
    return render(request, 'check-out.html', context)


#class Payment(View):
#    def get(self, *args, **kwargs):
#        form = PaymentForm()
#        category = Category.objects.all()
#        context = {
#            'form': form,
#            'category': category,
#        }
#        return render(self.request, "pament.html", context)
#
#    def post(self, *args, **kwargs):
#        form = PaymentForm(self.request.POST or None)
#        try:
#            if form.is_valid():
#
#                payment_option = form.cleaned_data.get('payment_option')
#
#                if payment_option == 'CD':
#                    return redirect('/order/paymentcash/', payment_option='cash on delivery(lipa mzigo ukiuona)')
#                else:       
#                    messages.warning(self.request, "Invalid payment option selected")
#                    return redirect('/order/payment/')    
#        except ObjectDoesNotExist:
#            messages.warning(self.request, "You do not have an active order ")
#        

#class PaymentCash(View):
#    def post(self, *args, **kwargs):
#        category = Category.objects.all()
#        ordercode = Order.objects.get(user=self.request.user)
#        order = Order.objects.get(user=self.request.user)
#        timestamp = timezone.now()
#
#        try:
#            payment = DeliveredPayment()
#            payment.user = self.request.user
#            payment.timestamp = timezone.now()
#            payment.save()
#
#            messages.success(self.request, "your order was successful!")
#            context = {'category': category,
#                       'ordercode': ordercode
#                       }
#            return render(request, 'order_completed.html', context)
#            #return redirect("/")
#
#        except ObjectDoesNotExist:
#            messages.error(self.request, "A serious error occurred. We have been notifed")
#            return redirect("/")

    
