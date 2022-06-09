from django.shortcuts import render, redirect
from .models import PaymentGateway, Invoice, InvoiceDetail
from product_module.models import CartItem, Product
from datetime import date, datetime
from django.db import transaction
from django.urls import reverse

# Create your views here.
def confirmpayment(request):
    if request.method == "POST":
        token = request.POST.get("token")
        amount = request.POST.get("amount")

    # clean up
    token = token.strip()
    amount = float(amount)

    try:
        with transaction.atomic():
            # open an atomic transaction, i.e. all successful or none
            make_payment(token, amount)
            maintain_invoice(request, token, amount)
    except Exception as e:
        request.session["message"] = str(e)
        return redirect(reverse('error_page'))
    
    else:
        request.session["message"] = f"Payment successfully completed with NRs. {amount} from your balance!"
    return redirect(reverse('success_page'))
