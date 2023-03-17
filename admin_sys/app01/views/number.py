from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from django import forms



# 靓号列表
def number_list(request):
    data_dict = {}
    value = request.GET.get('q')
    if value:
        data_dict["mobile__contains"] = value
    queryset = models.PrettyNum.objects.filter(**data_dict)
    return render(request, "number_list.html", {"queryset": queryset})


# 新建靓号
class NumberForm(forms.ModelForm):
    class Meta:
        model = models.PrettyNum
        # fields = ["id", "mobile", "price", "lever", "status"]
        # exclude = ["mobile"]
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def number_add(request):
    if request.method == "GET":
        form = NumberForm()
        return render(request, "number_add.html", {"form": form})

    form = NumberForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/number/list/")
    return render(request, "number_add.html", {"form": form})


# 靓号编辑
def number_edit(request, nid):
    row_data = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = NumberForm(instance=row_data)
        return render(request, "number_edit.html", {"form": form})

    # 校验
    form = NumberForm(data=request.POST, instance=row_data)
    if form.is_valid():
        # 当有instance参数时，form.save()会对数据进行更新
        form.save()
        return redirect("/number/list")
    return render(request, "number_edit.html", {"form": form})


# 靓号删除
def number_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/number/list/")