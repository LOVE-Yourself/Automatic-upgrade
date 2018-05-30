import xadmin
from .models import Version,UploadFile

class VersionAdmin(object):

    list_display = ['name', 'file','number','add_time']
    search_fields = ['name','file','number']
    list_filter = ['name', 'file','number','add_time']

class UploadFileAdmin(object):

    list_display = ['name', 'file', 'detail','add_time']
    search_fields = ['name', 'file', 'detail']
    list_filter = ['name', 'file', 'detail','add_time']


xadmin.site.register(Version, VersionAdmin)
xadmin.site.register(UploadFile,UploadFileAdmin)
