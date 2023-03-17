from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms


# 部门列表
def depart_list(request):
    queryset = models.Department.objects.all()

    return render(request, "depart_list.html", {'queryset': queryset})


# 添加部门
def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    # 获取用户post提交得数据
    title = request.POST.get("title")
    # 保存到数据库
    models.Department.objects.create(title=title)
    # 重定向回部门列表
    return redirect("/depart/list/")


def depart_delete(request):
    nid = request.GET.get("nid")
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


# 编辑部门
def depart_edit(request, nid):
    if request.method == "GET":
        title = models.Department.objects.filter(id=nid).first().title
        return render(request, 'depart_edit.html', {"title": title})

    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list/")

# 文件上传
# def depart_multi(request):
    # 批量删除（excel文件）


