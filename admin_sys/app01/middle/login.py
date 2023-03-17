from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect


class Login(MiddlewareMixin):
    def process_request(self, request):
        # 排除登录页面
        if request.path_info in ["/login/", "/img/verify_img/"]:
            return
        login = request.session.get("info")
        if not login:
            return redirect("/login/")
        return
