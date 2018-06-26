from datetime import datetime

from django.db import models
from operation.models import Version
# Create your models here.
class VesionFile(models.Model):
    version = models.ForeignKey(Version, verbose_name=u'所属版本')
    name = models.CharField(default='test.iso', max_length=20, verbose_name=u'文件名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'版本文件'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class UploadFile(models.Model):
    versionfile = models.ForeignKey(VesionFile,null=True,blank=True,verbose_name=u'所属版本文件')
    number = models.CharField(default='1.0',max_length=20,verbose_name=u'版本号')
    file = models.FileField(upload_to='UpFile/%Y/%m',verbose_name=u'文件路径')
    detail = models.TextField(verbose_name=u'上传文件的更改描述')

    add_time = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    class Meta:
        verbose_name = u'上传文件'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.number