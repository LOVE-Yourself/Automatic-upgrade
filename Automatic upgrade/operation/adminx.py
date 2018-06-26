import xadmin
from .models import Version,Machine,MachineChangeStatus,DeferentFileNameVesion

class MachineAdmin(object):
    list_display = ['machine_sn', 'version_sn','add_time']
    search_fields = ['machine_sn', 'version_sn']
    list_filter = ['machine_sn', 'version_sn','add_time']

class VersionAdmin(object):
    list_display = ['name', 'file','number','edition_sn','add_time']
    search_fields = ['name','file','number','edition_sn']
    list_filter = ['name', 'file','number','edition_sn','add_time']


class MachineChangeStatusAdmin(object):
    list_display = ['machine', 'version_sn','is_update','add_time']
    search_fields = ['machine', 'version_sn','is_update']
    list_filter = ['machine', 'version_sn','is_update','add_time']

class DeferentFileNameVesionAdmin(object):
    list_display = ['version', 'filename','add_time']
    search_fields = ['version', 'filename']
    list_filter = ['version', 'filename','add_time']



xadmin.site.register(Machine,MachineAdmin)
xadmin.site.register(Version, VersionAdmin)
xadmin.site.register(MachineChangeStatus, MachineChangeStatusAdmin)
xadmin.site.register(DeferentFileNameVesion, DeferentFileNameVesionAdmin)


