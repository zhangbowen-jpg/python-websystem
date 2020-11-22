from django.shortcuts import render
from django.http import JsonResponse
from lsql.models import Operator,Zhenghe
# Create your views here.
import pandas as pd
import time
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def operator_echarts(request):
    data = pd.read_excel(os.path.join(BASE_DIR, 'echart', 'operator.xlsx'))
    data_dict = data.to_dict(orient='split')
    time.sleep(5)
    return JsonResponse({'data':data_dict['data']})

def zhenghe_echarts(request):
    data = pd.read_excel(os.path.join(BASE_DIR, 'echart', 'zhenghe.xlsx'))
    data_dict = data.to_dict(orient='split')
    time.sleep(5)
    return JsonResponse({'data':data_dict['data']})

