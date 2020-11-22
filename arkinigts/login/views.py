from django.shortcuts import render
from login.models import *
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def log_in(request):
    managername = request.POST.get('name')
    password = request.POST.get('password')
    user_check = Manager.objects.filter(managername=managername,password=password)
    if user_check:
        return JsonResponse({'data':'登陆成功','check':True})
    else :
        return JsonResponse({'data':'登陆失败','check':False})

@csrf_exempt
def establish(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    nickname = '临时用户'
    query_rs = Manager.objects.filter(managername__istartswith=name)
    if query_rs:
        return JsonResponse({'data':'用户已存在'})
    else :
        Manager(managername=name,password=password,nickname=nickname).save()
        return JsonResponse({'data':'用户添加成功'})

# @csrf_exempt 代表函数可以跨域访问
def manager_page(request):
    return render(request,'manage.html')

def to_login(request):
    return render(request,'login.html')