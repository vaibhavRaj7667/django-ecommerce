from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import*
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .models import*
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Product, Cart, CartItem


def createUser(request):
    if request.method == 'POST':
        form =userCreationForm(request.POST)
        email= request.POST.get('email')
        if User.objects.filter(email=email).exists:
            messages.error(request, "Email already exists. Please use a different email.")
        elif form.is_valid():
            form.save()
    else:
        form = userCreationForm()
    return render(request,'home.html',{'form':form})




def LoginUser(request):
    if request.method == "POST":
        email = request.POST.get("email")  
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)  
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.") 
            return render(request, 'html/login.html')  

        username = user.username 

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user) 

            return redirect('Home') 
        else:
            messages.error(request, "Invalid email or password.")

    else:
    
        return render(request,'html/login.html')


    return render(request, 'html/login.html')


def registerUser(request):
    if request.method =="POST":
        form = userCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('LoginUser')
    else:
        form = userCreationForm()
    return render(request,'html/register.html',{'form':form})



def LogoutUser(request):
    logout(request)
    return render(request,'html/login.html')

    


def Home(request,slug=None):
    Categorys = Category.objects.get(slug ="kurti")
    kurtis = Product.objects.filter(category=Categorys)

    if slug:
        Categorys_ = Category.objects.get(slug =slug)
        products = Product.objects.filter(category=Categorys_)
    else:
        products = Product.objects.all()
    
    return render(request,'html/home.html',{'kurtis':kurtis[:3],'products':products[:8]})


def products(request,slug,price=None):
    Categorys = Category.objects.get(slug=slug)
    items = Product.objects.filter(category = Categorys)

    if price:
        items = items.filter(price__lte=price)
    return render(request,'html/product.html',{'items':items,'Categorys':Categorys})



def items(request,slug_):
    item = get_object_or_404(Product,slug=slug_)
    return render(request,'html/items.html',{'item':item})



def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
        cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart = get_or_create_cart(request)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.name} quantity increased in your cart.")
    else:
        messages.success(request, f"{product.name} added to your cart successfully.")
    return redirect('items',slug_=product.slug)

def remove_from_cart(request, slug):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, slug=slug)
    CartItem.objects.filter(cart=cart, product=product).delete()
    messages.success(request, f"{product.name} Delete from cart")
    # return JsonResponse({"message": "Product removed from cart successfully"})
    return redirect('view_cart')


def view_cart(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'html/cart.html', {'cart_items': cart_items, 'total_price': total_price})



def place_order(request):
    
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            if not cart.items.exists():
                messages.error(request, "Your cart is empty! Please add items to your cart before placing an order.")
                return redirect('view_cart')  
        except Cart.DoesNotExist:
            return render(request, 'html/create_order.html', {
                'error': 'No active cart found! Please add items to your cart first.',
            })

        if request.method == 'POST':
        
            address = request.POST.get('address', '').strip()
            if not address:
                return render(request, 'html/create_order.html', {
                    'cart': cart,
                    'error': 'Delivery address is required.',
                })

        
            order = Order.objects.create(
                user=request.user,
                cart = cart,
                address=address
            )

        
            for cart_item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price,  
                )

        
            order.calculate_total()

        
            cart.items.all().delete()

            messages.success(request, 'Your order has been successfully placed!')
            return render(request, 'html/create_order.html', {'order': order})

        
        return render(request, 'html/create_order.html', {
            'cart': cart,
        })
    
    else:
        messages.error(request,"you are not login to create a order")
        return redirect('LoginUser')





def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'html/order_list.html', {'orders': orders})



# def order_detail(request, order_id):
#     order = get_object_or_404(Order, id=order_id, user=request.user)
#     return render(request, 'html/order_detail.html', {'order': order})



