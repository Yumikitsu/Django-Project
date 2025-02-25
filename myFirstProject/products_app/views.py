from django.shortcuts import render, redirect
from .models import OrderList
from django.contrib import messages
from groceries_app import views as groceries

# Create your views here.
def product_list(request):
    products = {"dairy": ["milk", "yogurt", "cheese", "butter"],
                "beverages": ["soda", "juice"],
                "vegetables": ["ginger", "lettuce", "spinach"],
                "fruits": ["bananas", "apples", "grapes"]}
    
    return render(request, "products_list.html", products)

def order(request):
    if request.method == 'POST':
        prod_list = request.POST.getlist('products')
        prod_str = ",".join(prod_list)
        order_data = OrderList(wholelist=prod_str, username=groceries.usrnme)
        order_data.save()
        messages.success(request, "Order created successfully: " + prod_str)
        return redirect("loggedin")
    else:
        return render(request, "product_list.html")