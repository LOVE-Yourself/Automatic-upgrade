import xadmin
from .models import Version,UploadFile,VesionFile,Machine

class MachineAdmin(object):
    list_display = ['machine_sn', 'version_sn','add_time']
    search_fields = ['machine_sn', 'version_sn']
    list_filter = ['machine_sn', 'version_sn','add_time']

class VersionAdmin(object):
    list_display = ['name', 'file','number','edition_sn','add_time']
    search_fields = ['name','file','number','edition_sn']
    list_filter = ['name', 'file','number','edition_sn','add_time']

class VesionFileAdmin(object):
    list_display = ['version','name','add_time']
    search_fields = ['version','name']
    list_filter = ['version','name','add_time']

class UploadFileAdmin(object):
    list_display = ['versionfile','number', 'file', 'detail','add_time']
    search_fields = ['versionfile','number', 'file', 'detail']
    list_filter = ['versionfile','number', 'file', 'detail','add_time']


xadmin.site.register(Machine,MachineAdmin)
xadmin.site.register(Version, VersionAdmin)
xadmin.site.register(VesionFile,VesionFileAdmin)
xadmin.site.register(UploadFile,UploadFileAdmin)

