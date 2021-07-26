from django.shortcuts import render, HttpResponse
from .models import Decimal
import math
from .util import decimal

def cde(request):
    try:
        pre = float()
        pre1 = float()
        if request.method == 'POST':
            if request.POST.get('number'):
                number = float(request.POST['number'])
                prec = int(request.POST['prec'])
                if prec == 2:
                    pre = decimal(number,prec)
                    Decimal(number=number, pre=pre, pre1=pre1).save()
                    return HttpResponse(f"inserted successfully{pre}")
                elif prec == 3:
                    pre1 = decimal(number,prec)
                    Decimal(number=number, pre=pre, pre1=pre1).save()
                    return HttpResponse(f"inserted successfully{pre1}")
    except Exception as e:
        print(e)
    return render(request, "index.html")

def retrieve(request):
    retrieve = Decimal.objects.all()
    return render(request, 'table.html', {'precision_decimal': retrieve})


# Create your views here.
