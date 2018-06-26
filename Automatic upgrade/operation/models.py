from datetime import datetime

from django.db import models

from  users.models import UserProfile
# from ..course.models import Course
# from Lyonline.users import UserProfile

class Machine(models.Model):
    machine_sn = models.CharField(max_length=20,unique=True,null=True,blank=True,verbose_name=u'机器号')
    version_sn = models.CharField(default='2.0.1',max_length=20,verbose_name=u'版本号')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'远程机器'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.machine_sn

class Version(models.Model):
    name = models.CharField(default='课程2.0',max_length=20,verbose_name=u'版本名')
    edition_sn = models.CharField(default='2.0.1',max_length=20,verbose_name=u'版本号')
    file = models.FileField(null=True,blank=True,upload_to='Version/%Y/%m',verbose_name=u'版本所在位置')
    # number = models.IntegerField(default=23,null=True,blank=True,verbose_name=u'文件个数')
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    is_changefile = models.BooleanField(default=False,verbose_name=u'更新文件')

    class Meta:
        verbose_name = u'系统版本'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.edition_sn

#记录机器更新状态
class MachineChangeStatus(models.Model):
    machine = models.ForeignKey(Machine,verbose_name=u'机器')
    version_sn = models.CharField(default='2.0.1',max_length=20,verbose_name=u'版本号')
    is_update = models.BooleanField(default=False,verbose_name=u'是否更新')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'机器更新状态'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.version_sn

#记录这个版本与上一个版本的文件变化
class DeferentFileNameVesion(models.Model):
    version = models.ForeignKey(Version,verbose_name=u'当前版本')
    filename = models.CharField(max_length=200,verbose_name=u'更改的文件')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'版本文件变化'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.filename




