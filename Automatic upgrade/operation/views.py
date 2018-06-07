import os,shutil,json

from django.shortcuts import render
from django.views.generic import View
from django.http import FileResponse,HttpResponse

from Lyonline.settings import BASE_DIR
from .models import Version,UploadFile,Machine,VesionFile
from  utils.util import Zipfolder

class ResourceView(View):
    def get(self,request,machine_sn):
        #机器号  取出版本号2.0.1
        machine = Machine.objects.get(machine_sn = machine_sn)
        #机器当前的版本号
        mac_vsn = machine.version_sn
        version = Version.objects.order_by('-add_time')[0]
        #最新上传的版本号
        v_sn = version.edition_sn
        if int(mac_vsn.split('.')[1]) < int(v_sn.split('.')[1]):
            print('---->强制升级')
            #强制升级
            file_path = version.file
            filname = version.name
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            source_path = os.path.join(MEDIA_ROOT,str(file_path))
            file = open(source_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filname)
            return response

        elif int(mac_vsn.split('.')[2]) < int(v_sn.split('.')[2]):
            #选择升级
            print('---->选择升级')
            return HttpResponse("{'status':'chance'}", content_type='application/json')
        else:
            #不用升级
            return HttpResponse("{'status':'no_change'}", content_type='application/json')

        #如果版本号2.0.2 选择更新
        #2.1.2 必须更新

#获取版本下的更新文件
class ResourceView1(View):
    def get(self,request,machine_sn):
        #脚本默认机器号为1
        # 通过机器号    版本号
        machine = Machine.objects.get(machine_sn=machine_sn)
        version_sn = machine.version_sn
        version  = Version.objects.get(edition_sn=version_sn)
        version_files = VesionFile.objects.filter(version=version)
        #有可能没
        if version_files.count == 0:
            # 不用升级
            return HttpResponse("{'status':'no_change'}", content_type='application/json')
        new_files = []
        file_dict = {}
        for vs_file in version_files:
            uploadfiles = UploadFile.objects.all()
            uploadfiles = uploadfiles.filter(versionfile=vs_file)
            #获取最新的文件
            uploadfile = uploadfiles.order_by('-add_time')[0]
            file_dict['name'] = vs_file.name
            file_dict['file'] = uploadfile
            new_files.append(file_dict)
        #把那几个修改的文件打包``
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        newname = os.path.join(MEDIA_ROOT, 'Change_file')
        # if os.path.exists()
        for file in new_files:
            file_path = file['file'].file
            source_path = os.path.join(MEDIA_ROOT,str(file_path))
            capy_file = os.path.join(newname,file['name'])
            shutil.copyfile(source_path, capy_file)
        zipfolder = Zipfolder()
        # 先判断有没有压缩文件,有删除
        zipfolder.rm_zip(newname + '.zip')
        #压缩打包文件
        zipfolder.zip_ya(newname)
        #清空chang_file
        zipfolder.rm_file(newname)
        file = open(newname + '.zip', 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format('change_file.zip')
        return response

        # tmp_dl_path = os.path.join(source_path, filename)
        #写到一个文件夹中再返回 压缩文件给我
        # utilities.toZip(source_path, filename)

class ReturnIsUpdateView(View):
    def get(self,request,machine_sn):
        #更新
        version = Version.objects.order_by('-add_time')[0]
        # 将机器号  和版本hao相关联
        machine = Machine.objects.filter(machine_sn=machine_sn)[0]
        machine.version_sn = version.edition_sn
        machine.save()
        file_path = version.file
        filname = version.name
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
        source_path = os.path.join(MEDIA_ROOT, str(file_path))
        file = open(source_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filname)
        return response









