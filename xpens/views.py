from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Expense

def index(request):
    latest_expense_list = Expense.objects.order_by('-date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_expense_list': latest_expense_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, xpens_id):
    return HttpResponse("You're looking at Expense %s." % xpens_id)
