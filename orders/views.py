from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import ReturnPolicyForm
from django.contrib.auth.decorators import login_required
from basket.basket import Basket
from account.models import Address
from .models import Order, OrderItem,ReturnPolicy
from django.core.mail import send_mail
from django.contrib import messages






def add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":

        order_key = request.POST.get("order_key")
        user_id = request.user.id
        baskettotal = basket.get_total_price()
        full_name1 = str(request.user.name)
        mobile = str(request.user.mobile)

        # Check if order exists
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Order.objects.create(
                user_id=user_id,
                full_name=full_name1,
                phone=mobile,
                total_paid=baskettotal,
                order_key=order_key,
                order_status="Received"
            )
            order_id = order.pk
            product_details = ""

            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"]
                )

                # Include product details in the email message
                product_details += f"<tr><td>{item['product']}</td><td>{item['qty']}</td><td>₹{item['price']}</td></tr>"

        # Create an HTML table for the product details
        product_table = f"<table><tr><th>Product</th><th>Quantity</th><th>Price</th></tr>{product_details}</table>"

        order_details_message = f"""<p>Order #{order_id} successfully placed for {full_name1}.</p>
        <p>Total amount paid: ₹{baskettotal}</p>
        {product_table}"""

        send_mail(
            'Order Confirmation',
            order_details_message,
            'rahulsuregaonkar@gmail.com',  # Change to your email address
            [request.user.email],  # Send to the user's email address
            fail_silently=False,
            html_message=order_details_message,  # Specify the HTML content
        )

        # Use messages framework to store the message
        messages.success(request, "Order placed successfully!")

        response = JsonResponse({"success": "Return something"})
        return response


def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders



def return_book(request, order_id):
    order = Order.objects.get(id=order_id)
    form = ReturnPolicyForm(initial={'order': order})
    return_policy = ReturnPolicy.objects.filter(order=order).first()
    
    if return_policy and return_policy.is_accepted:
        success_message = "Return request accepted and refund is on the way for more assistance call."
        return render(request, 'account/dashboard/success.html', {'success_message': success_message})
    
    if return_policy and not return_policy.is_accepted:
        success_message = "Return request is not accepted and for more assistance call."
        return render(request, 'account/dashboard/success.html', {'success_message': success_message})
    
    return render(request, 'account/dashboard/return.html', {'form': form, 'order': order})


@login_required
def return_book_submit(request, order_id):
    order = Order.objects.get(id=order_id)
    
    if request.method == 'POST':
            form = ReturnPolicyForm(request.POST)
            if form.is_valid():
                return_policy = form.save(commit=False)
                return_policy.order = order
                return_policy.save()
                # You can perform additional actions here if needed
                success_message = "Return request submitted successfully."
                return render(request, 'account/dashboard/success.html', {'success_message': success_message})
    else:
        form = ReturnPolicyForm(initial={'order': order})
    
    return render(request, 'account/dashboard/return.html', {'form': form, 'order': order})