from django.db import models


# 管理员表
class Admin(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)


# Create your models here.
# 部门表
class Department(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)

    # CharField类型必须设置长度
    def __str__(self):
        return self.title


# 员工表
class UserInfo(models.Model):
    """ 员工表 """
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="入职时间")
    # choices
    gender_choices = (
        (1, "男"),
        (2, "女")
    )
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices, null=True, blank=True)
    # 级联删除 详看视频p21 表结构的创建
    # 默认生成列名为 depart_id
    depart = models.ForeignKey(verbose_name="部门", to='Department', to_field='id', on_delete=models.CASCADE, null=True,
                               blank=True)


# 靓号管理
class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name="号码", max_length=11)
    price = models.IntegerField(verbose_name="价格")

    lever_choices = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级"),
        (4, "四级")
    )
    lever = models.SmallIntegerField(verbose_name="级别", choices=lever_choices, default=1)

    status_choices = (
        (1, "已占用"),
        (2, "未占用")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
