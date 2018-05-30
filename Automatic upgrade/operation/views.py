import os

from django.shortcuts import render
from django.views.generic import View
from django.http import FileResponse

from Lyonline.settings import BASE_DIR
from .models import Version,UploadFile
from  utils.util import ZipUtilities

class ResourceView(View):
    def get(self,request):
        version = Version.objects.all()[1]
        number = '2.0.1'
        # if
        # for version in versions:
        #
        #     version.name.split
        # utilities = ZipUtilities()
        # files = UploadFile.objects.filter(version=version)
        # for file in files:
        #     file_path = files.file
        #     filename = files.name
        #     MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        #     source_path = os.path.join(MEDIA_ROOT, str(file_path))
        #     tmp_dl_path = os.path.join(source_path, filename)
        #     utilities.toZip(tmp_dl_path, filename)

        file_path = version.file
        filname = version.name
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        source_path = os.path.join(MEDIA_ROOT,str(file_path))
        print('-->',source_path)
        file = open(source_path, 'rb')

        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filname)
        return response





