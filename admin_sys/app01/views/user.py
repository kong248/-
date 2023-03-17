from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms
# 用户列表
def user_list(request):
    queryset = models.UserInfo.objects.all()
    return render(request, 'user_list.html', {"queryset": queryset})


# 新建用户
def user_add(request):
    queryset = models.UserInfo.objects.all()
    return render(request, "user_add.html", {"queryset": queryset})


# modelform表单



class Userform(forms.ModelForm):
    name = forms.CharField(min_length=3, label="姓名")

    class Meta:
        model = models.UserInfo
        fields = ["name", "password", "age", "account", "create_time", "gender", "depart"]

    # 重点 样式更改
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_modelformadd(request):
    if request.method == "GET":
        form = Userform()
        return render(request, "user_modelformadd.html", {"form": form})

    # 提交表单
    # 数据校验
    form = Userform(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    # 验证失败
    return render(request, "user_modelformadd.html", {"form": form})


# 编辑用户
def user_edit(request, nid):
    row_data = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = Userform(instance=row_data)  # instance会把获取的数据自动填充到每一栏
        return render(request, "user_edit.html", {"form": form})

    form = Userform(data=request.POST, instance=row_data)
    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, "user_edit.html", {"form": form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")
