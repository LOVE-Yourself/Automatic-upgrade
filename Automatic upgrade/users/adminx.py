import xadmin
#from .models import EmailVerifyRecord,Banner

from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    show_bookmarks = False

class GlobalSettings(object):
    show_bookmarks = False
    site_title = '自动升级后台'
    site_footer = '拓叭吧'
    menu_style = 'accordion'#下拉菜单


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)