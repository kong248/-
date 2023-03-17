from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms
from django.core.exceptions import ValidationError
# md5加密加盐
import hashlib
from django.conf import settings


def md5(data):
    # 加盐
    salt = settings.SECRET_KEY
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(data.encode("utf-8"))
    return obj.hexdigest()


# 管理员管理
def admin_list(request):
    """# 判断是否已经登录账号(统一写到中间件)
    login = request.session.get("info")
    if not login:
        return redirect("/login/")"""

    queryset = models.Admin.objects.all()
    return render(request, "admin_list.html", {'queryset': queryset})


# 添加管理员
class AdminForm(forms.ModelForm):
    comfirm_password = forms.CharField(label="确认密码", widget=forms.PasswordInput)

    class Meta:
        model = models.Admin
        fields = "__all__"
        widgets = {"password": forms.PasswordInput(render_value=True)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

    # 钩子方法验证”确认密码“字段
    def clean_password(self):
        pa = self.cleaned_data.get("password")
        return md5(pa)

    def clean_comfirm_password(self):
        pa = self.cleaned_data.get("password")
        cpa = self.cleaned_data.get("comfirm_password")
        cpa = md5(cpa)
        if pa != cpa:
            raise ValidationError("密码不一致")
        return cpa


def admin_add(request):
    if request.method == "GET":
        form = AdminForm()
        return render(request, "admin_add.html", {"form": form})

    form = AdminForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "admin_add.html", {"form": form})


# 编辑
def admin_edit(request, nid):
    row_data = models.Admin.objects.filter(id=nid).first()
    if request.method == "GET":
        form = AdminForm(instance=row_data)
        return render(request, "admin_edit.html", {"form": form})

    form = AdminForm(data=request.POST, instance=row_data)
    if form.is_valid():
        form.save()
        return redirect("/admin/list/")
    return render(request, "admin_edit.html", {"form": form})


# 删除
def admin_delete(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect("/admin/list/")
