"""day16wupeiqi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app01.views import admin, depart, login, number, user


urlpatterns = [
    # 管理员界面
    #path('admin/', admin.site.urls),

    # 部门管理
    path("depart/list/", depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),  # django中url传值的第二种方式
    path('/depart/multi/ ', depart.depart_multi),
    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/modelform/add/', user.user_modelformadd),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),

    # 靓号管理
    path('number/list/', number.number_list),
    path('number/add/', number.number_add),
    path('number/<int:nid>/edit/', number.number_edit),
    path('number/<int:nid>/delete/', number.number_delete),

    # 管理员账户
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    # 登录
    path('login/', login.login),
    path('logout/', login.logout),
    path('img/verify_img/', login.img),
]
