from django.contrib import messages
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from User.forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from User.models import UserProfile
from order.models import Order, OrderProduct
from shop.models import Category, Comment, FAQ


# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        category = Category.objects.all()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                #create profile
                current_user = request.user
                data = UserProfile()
                data.user_id=current_user.id
                data.image="img/avatar-2.png"
                data.save()
                messages.success(request, 'Account was created')


                return redirect('/user/update/') 
            else:
                messages.warning(request, form.errors)
                return redirect('shop:signup')

        context = {'form': form,
                   'category': category
                   }
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        category = Category.objects.all()
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')


            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')

            else:
                messages.info(request, 'username OR password is incorrect')

        context = {'category': category}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('shop:login')


def profile(request):
    current_user = request.user
    category = Category.objects.all()
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile
               }
    return render(request, 'user_profile.html', context)


def update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return HttpResponseRedirect('/user/profile')

    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'category': category,
                   'user_form': user_form,
                   'profile_form': profile_form
                   }
        return render(request, 'user_update.html', context)


def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated')
            return HttpResponseRedirect('/user/profile')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {'category': category,
                   'form': form
                   }
        return render(request, 'user_password.html', context)


def user_orders(request):
    category = Category.objects.all()
    current_user = request.user
    orders = Order.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'orders': orders
               }
    return render(request, 'user_orders.html', context)


def user_orderdetail(request, id):
    category = Category.objects.all()
    current_user = request.user
    order = Order.objects.get(user_id=current_user.id, id=id)
    orderitems = OrderProduct.objects.filter(order_id=id)
    context = {'category': category,
               'order': order,
               'orderitems': orderitems
               }
    return render(request, 'user_detail.html', context)


def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    order_product = OrderProduct.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'order_product': order_product
               }
    return render(request, 'order_product.html', context)


def user_comment(request):
    category = Category.objects.all()
    current_user = request.user
    comment = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'comment': comment
               }
    return render(request, 'user_comment.html', context)


def user_deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(user_id=current_user.id, id=id).delete()
    messages.success(request, "comment deleted...")
    return HttpResponseRedirect('/user/comment')


def faq(request):
    category = Category.objects.all()
    faq = FAQ.objects.filter(status="True").order_by("ordernumber")
    context = {'category': category,
               'faq': faq
               }
    return render(request, 'faq.html', context)