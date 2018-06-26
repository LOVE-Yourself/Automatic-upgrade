import xadmin
from .models import UploadFile,VesionFile

class VesionFileAdmin(object):
    list_display = ['version','name','add_time']
    search_fields = ['version','name']
    list_filter = ['version','name','add_time']

class UploadFileAdmin(object):
    list_display = ['versionfile','number', 'file', 'detail','add_time']
    search_fields = ['versionfile','number', 'file', 'detail']
    list_filter = ['versionfile','number', 'file', 'detail','add_time']

xadmin.site.register(VesionFile,VesionFileAdmin)
xadmin.site.register(UploadFile,UploadFileAdmin)