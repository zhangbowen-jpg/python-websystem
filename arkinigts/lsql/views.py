from django.shortcuts import render
from django.http import JsonResponse
from lsql.models import Operator,Zhenghe
import time
from django.forms.models import model_to_dict
# Create your views here.

def query_op(request):
    result = Operator.objects.filter(name=request.GET.get('choose'))
    list_op = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id', 'name', 'place', 'health', 'attack', 'defined','magic', 'a_time', 's_cost', 'blocked','between']))
    return JsonResponse({'data':list_op})

def query_zh(request):
    result = Zhenghe.objects.filter(name=request.GET.get('choose'))
    list_zhenghe = []
    for rs in result:
        list_zhenghe.append(model_to_dict(rs,fields=['id','name','level','power','attack','health','defined','magic','pace']))
    return JsonResponse({'data':list_zhenghe})

def Show_echarts(request):
    result = Operator.objects.filter(id__range=('1','200'))
    list_op = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id', 'name', 'place', 'health', 'attack', 'defined','magic', 'a_time', 's_cost', 'blocked','between']))
    time.sleep(2.5)
    return JsonResponse({'data': list_op})
def Show_zhenghe(request):
    result = Zhenghe.objects.filter(id__range=('1', '200'))
    list_op = []
    for rs in result:
        list_op.append(model_to_dict(rs,fields=['id','name','level','power','attack','health','defined','magic','pace']))
    time.sleep(2.5)
    return JsonResponse({'data': list_op})

def operator_echart(request):
    return render(request,'echarts.html')

def zhenghe_echart(request):
    return render(request,'zhenghe_echarts.html')

def operator_health_echart(request):
    result = Operator.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_health = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','health']))
    for i in list_op:
        list_id.append(i['id'])
        list_health.append(i['health'])
    return JsonResponse({'id':list_id,'health':list_health})

def operator_attack_echart(request):
    result = Operator.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_attack = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','attack']))
    for i in list_op:
        list_id.append(i['id'])
        list_attack.append(i['attack'])
    return JsonResponse({'id':list_id,'attack':list_attack})

def operator_defined_echart(request):
    result = Operator.objects.filter(id__range=('1', '152'))
    list_op = []
    list_id =[]
    list_defined = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','defined']))
    for i in list_op:
        list_id.append(i['id'])
        list_defined.append(i['defined'])
    return JsonResponse({'id':list_id,'defined':list_defined})

def operator_magic_echart(request):
    result = Operator.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_magic = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','magic']))
    for i in list_op:
        list_id.append(i['id'])
        list_magic.append(i['magic'])
    return JsonResponse({'id':list_id,'magic':list_magic})

def zhenghe_health_echart(request):
    result = Zhenghe.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_health = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','health']))
    for i in list_op:
        list_id.append(i['id'])
        list_health.append(i['health'])
    return JsonResponse({'id':list_id,'health':list_health})

def zhenghe_attack_echart(request):
    result = Zhenghe.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_attack = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','attack']))
    for i in list_op:
        list_id.append(i['id'])
        list_attack.append(i['attack'])
    return JsonResponse({'id':list_id,'attack':list_attack})

def zhenghe_defined_echart(request):
    result = Zhenghe.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_defined = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','defined']))
    for i in list_op:
        list_id.append(i['id'])
        list_defined.append(i['defined'])
    return JsonResponse({'id':list_id,'defined':list_defined})

def zhenghe_magic_echart(request):
    result = Zhenghe.objects.filter(id__range=('1', '200'))
    list_op = []
    list_id =[]
    list_magic = []
    for rs in result:
        list_op.append(model_to_dict(rs, fields=['id','magic']))
    for i in list_op:
        list_id.append(i['id'])
        list_magic.append(i['magic'])
    return JsonResponse({'id':list_id,'magic':list_magic})