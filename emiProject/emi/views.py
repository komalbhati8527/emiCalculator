from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

# Create your views here.
def emicalculator(request):
    title = {"title":"Emi calculator"}
    return render(request, "emicalculator.html", title)

@csrf_exempt
def emiResult(request):
    # formula P x R x (1+R)^N / [(1+R)^N-1]
    loanAmount = request.POST.get("loanAmount")
    loanTenure = request.POST.get("loanTenure")
    loanInterest = request.POST.get("loanInterest")
    tenure = int(loanTenure)*12
    rate = float(loanInterest)/12/100
    principal = int(loanAmount)
    power = pow(1+rate, tenure)/(pow(1+rate, tenure) - 1)
    emi = principal * rate * power
    total_interest = emi * tenure - principal
    total_amount = principal + total_interest
    response = {"emi": int(emi), "interest": int(total_interest), "total_amount": int(total_amount)}
    return JsonResponse({"data": response})

