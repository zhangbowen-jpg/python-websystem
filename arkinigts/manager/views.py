from django.shortcuts import render
from lsql.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def add_op(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    place = request.POST.get('place')
    health = request.POST.get('health')
    attack = request.POST.get('attack')
    defined = request.POST.get('defined')
    magic = request.POST.get('magic')
    a_time = request.POST.get('a_time')
    s_cost = request.POST.get('s_cost')
    blocked = request.POST.get('blocked')
    between = request.POST.get('between')
    query_ops = Operator.objects.filter(name__istartswith=name)
    query_ids = Operator.objects.filter(id__istartswith=id)
    if (query_ops | query_ids):
        return JsonResponse({'data':'添加失败，相关序号或姓名已经存在'})
    else :
        Operator(id=id,name=name,place=place,health=health,attack=attack,defined=defined,magic=magic,a_time=a_time,s_cost=s_cost,blocked=blocked,between=between).save()
        return JsonResponse({'data':'数据添加成功'})

@csrf_exempt
def update_op(request):
    name = request.POST.get('name')
    place = request.POST.get('place')
    health = request.POST.get('health')
    attack = request.POST.get('attack')
    defined = request.POST.get('defined')
    magic = request.POST.get('magic')
    a_time = request.POST.get('a_time')
    s_cost = request.POST.get('s_cost')
    blocked = request.POST.get('blocked')
    between = request.POST.get('between')
    if Operator.objects.filter(name=name):
        Operator.objects.filter(name=name).update(place=place,health=health,attack=attack,defined=defined,magic=magic,a_time=a_time,s_cost=s_cost,blocked=blocked,between=between)
        return JsonResponse({'data':'数据更新成功'})
    else:
        return JsonResponse({'data':'数据不存在'})

@csrf_exempt
def delete_op(request):
    name = request.POST.get('name')
    if Operator.objects.filter(name=name):
        Operator.objects.filter(name=name).delete()
        return JsonResponse({'data':'数据删除成功'})
    else:
        return JsonResponse({'data':'数据不存在'})
@csrf_exempt
def add_zhe(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    level = request.POST.get('level')
    power = request.POST.get('power')
    attack = request.POST.get('attack')
    health = request.POST.get('health')
    defined = request.POST.get('defined')
    magic = request.POST.get('magic')
    pace = request.POST.get('pace')
    query_zhs = Zhenghe.objects.filter(name__istartswith=name)
    query_ids = Zhenghe.objects.filter(id__istartswith=id)
    if (query_zhs | query_ids):
        return JsonResponse({'data':'添加失败，相关序号或名称已经存在'})
    else :
        Zhenghe(id=id,name=name,level=level,power=power,health=health,attack=attack,defined=defined,magic=magic,pace=pace).save()
        return JsonResponse({'data':'数据添加成功'})

@csrf_exempt
def update_zh(request):
    name = request.POST.get('name')
    level = request.POST.get('level')
    power = request.POST.get('power')
    attack = request.POST.get('attack')
    health = request.POST.get('health')
    defined = request.POST.get('defined')
    magic = request.POST.get('magic')
    pace = request.POST.get('pace')
    if Zhenghe.objects.filter(name=name):
        Zhenghe.objects.filter(name=name).update(level=level, power=power, health=health, attack=attack, defined=defined, magic=magic, pace=pace)
        return JsonResponse({'data':'数据更新成功'})
    else :
        return JsonResponse({'data':'数据不存在'})
@csrf_exempt
def delete_zh(request):
    name = request.POST.get('name')
    if Zhenghe.objects.filter(name=name):
        Zhenghe.objects.filter(name=name).delete()
        return JsonResponse({'data':'数据删除成功'})
    else :
        return JsonResponse({'data': '该数据不存在'})