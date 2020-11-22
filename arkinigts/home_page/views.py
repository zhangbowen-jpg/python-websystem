from django.shortcuts import render
from django.http import JsonResponse
import time
# Create your views here.


def home_page(request):
    time.sleep(2.5)
    return render(request,'homepage.html')

def zhenghe_page(request):
    return render(request,'zhenghe.html')

def operator_page(request):
    return render(request,'operator.html')

