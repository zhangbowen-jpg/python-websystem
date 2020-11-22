"""arkinigts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from lsql.views import *

urlpatterns = [ #子路由
    path('query_op/',query_op),
    path('query_zh/',query_zh),
    path('Show_echarts',Show_echarts),
    path('Show_zhenghe',Show_zhenghe),
    path('operator_echart',operator_echart),
    path('zhenghe_echart',zhenghe_echart),
    path('operator_health_echart',operator_health_echart),
    path('operator_attack_echart',operator_attack_echart),
    path('operator_defined_echart',operator_defined_echart),
    path('operator_magic_echart',operator_magic_echart),
    path('zhenghe_health_echart',zhenghe_health_echart),
    path('zhenghe_attack_echart',zhenghe_attack_echart),
    path('zhenghe_defined_echart',zhenghe_defined_echart),
    path('zhenghe_magic_echart',zhenghe_magic_echart),

]
