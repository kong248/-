from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms
# md5加密加盐
import hashlib
from django.conf import settings
from django.core.exceptions import ValidationError
from app01.static.app01.img.verify_img import check_code


def md5(data):
    # 加盐
    salt = settings.SECRET_KEY
    obj = hashlib.md5(salt.encode("utf-8"))
    obj.update(data.encode("utf-8"))
    return obj.hexdigest()


# 登录
class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", widget=forms.TextInput, required=True)
    password = forms.CharField(label="密码", widget=forms.PasswordInput, required=True)
    code = forms.CharField(label="验证码", widget=forms.PasswordInput, required=True)

    # 加盐
    def clean_password(self):
        return md5(self.cleaned_data.get("password"))


def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 先进行验证码的校验
        input_code = form.cleaned_data.pop("code")
        session_code = request.session.get("img_code", "")
        if input_code.upper() != session_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, "login.html", {"form": form})
        user = models.Admin.objects.filter(**form.cleaned_data).first()
        # 密码错误
        if not user:
            form.add_error("password", "密码错误")
            return render(request, "login.html", {"form": form})

        # 密码正确
        request.session["info"] = {"id": user.id, "name": user.username}
        request.session.set_expiry(60*60*24*7)
        return redirect("/admin/list")
    return render(request, "login.html", {"form": form})


# 注销
def logout(request):
    request.session.clear()
    return redirect("/login/")


# 验证码
from io import BytesIO


def img(request):
    photo, num = check_code()
    # 将验证码存入session以便校验
    request.session["img_code"] = num
    # 设置60秒超时时间
    request.session.set_expiry(60)
    # 将图片对象写入内存再进行获取
    stream = BytesIO()
    photo.save(stream, "png")
    stream.getvalue()
    return HttpResponse(stream.getvalue())
