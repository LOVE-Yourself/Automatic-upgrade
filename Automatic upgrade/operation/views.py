import os,shutil,json,zipfile

from django.shortcuts import render
from django.views.generic import View
from django.http import FileResponse,HttpResponse

from Lyonline.settings import BASE_DIR
from .models import Version,Machine,MachineChangeStatus,DeferentFileNameVesion
from  utils.util import Zipfolder

class ResourceView(View):
    def chanceversion(self,machine,version):
        #最新上传的版本号
        v_sn = version.edition_sn
        mac_vsn = machine.version_sn
        if int(mac_vsn.split('.')[1]) < int(v_sn.split('.')[1]):
            # 强制升级
            # 更改状态表
            machine_status = MachineChangeStatus()
            machine_status.machine = machine
            machine_status.version_sn = v_sn
            machine_status.is_update = True
            machine_status.save()

            file_path = version.file
            filname = version.name
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            source_path = os.path.join(MEDIA_ROOT, str(file_path))
            file = open(source_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filname)
            return response

        elif int(mac_vsn.split('.')[2]) < int(v_sn.split('.')[2]):
            # 选择升级
            return HttpResponse("{\"status\":\"chance\"}", content_type='application/json')
        else:
            # 不用升级
            #current_version_sn   new_version_sn
            current_version_sn = mac_vsn
            new_version_sn = v_sn
            return HttpResponse("{\"status\":\"no_change\",\"current_version_sn\":\"{0}\",\"new_version_sn\":\"{1}\"}".format(current_version_sn,new_version_sn), content_type='application/json')
    def get(self,request,machine_sn):
        version = Version.objects.order_by('-add_time')[0]
        #最新上传的版本号
        v_sn = version.edition_sn
        #机器号  取出版本号2.0.1
        machine = Machine.objects.get(machine_sn = machine_sn)
        mac_vsn = machine.version_sn
        #  最新的版本  遇到表里面的有 跳过更新
        try:
            #第一取 状态表中机器没有对应的状态
            machine_status = MachineChangeStatus.objects.filter(machine=machine)
            machine_Newstatus = machine_status.order_by('-add_time')[0]#取最新的状态
        except:
            return self.chanceversion(machine,version)
        if not machine_Newstatus.is_update:
            if machine_Newstatus.version_sn == v_sn:
                #证明 最新的版本它选择没更新
                current_version_sn = mac_vsn
                new_version_sn = v_sn
                return HttpResponse("{\"status\":\"no_change\",\"current_version_sn\":\"{0}\",\"new_version_sn\":\"{1}\"}".format(current_version_sn, new_version_sn), content_type='application/json')
            else:
                return self.chanceversion(machine,version)


class ReturnIsUpdateView(View):
    def machinestatus(self,version,machine_sn,isupdate):
        # 将机器号  和版本hao相关联
        machine = Machine.objects.filter(machine_sn=machine_sn)[0]
        machine.version_sn = version.edition_sn
        machine.save()
        # 更改状态表 只记录没更新的状态
        if not isupdate:
            machine_status = MachineChangeStatus()
            machine_status.machine = machine
            machine_status.version_sn = version.edition_sn
            machine_status.is_update = isupdate
            machine_status.save()

    def get(self,request,machine_sn):
        isupdate = request.GET.get('isupdate','')
        version = Version.objects.order_by('-add_time')[0]
        if isupdate:
            if isupdate == 'yes':
                #更新
                self.machinestatus(version,machine_sn,True)
                file_path = version.file
                filname = version.name
                MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
                source_path = os.path.join(MEDIA_ROOT, str(file_path))
                file = open(source_path, 'rb')
                response = FileResponse(file)
                response['Content-Type'] = 'application/octet-stream'
                response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filname)
                return response
            elif isupdate == 'no':
                self.machinestatus(version, machine_sn, False)

                return HttpResponse("{\"status\":\"no_update\"}", content_type='application/json')
            else:
                print('[+]:状态参数为空')

from Lyonline.settings import MEDIA_ROOT
from utils.util import compareManager
import shutil,hashlib
# from .models

#比较版本文件变化接口
class DisplayChangefileView(View):
    def get(self,request):
        try:
            version = Version.objects.order_by('-add_time')[0]
        except:
            print('当前文件库中没有版本')
            return HttpResponse("{\"status\":\"no_version\"}", content_type='application/json')

        if not version.is_changefile:
            #没有检测修改的文件
            #查看是否有 previous(上个版本的文件)
            previous_path = os.path.join(MEDIA_ROOT,'previous')
            #文件所在后台位置
            tbbzipPath = os.path.join(MEDIA_ROOT,str(version.file))
            #文件比较类
            comparemanager = compareManager()
            if not os.path.exists(previous_path):
                comparemanager.make_file(tbbzipPath,'previous')
            else:
                #解压索 为当前的
                current_path = os.path.join(MEDIA_ROOT, 'current')
                if os.path.exists(current_path):
                    #current 如果存在则删除
                    shutil.rmtree(current_path)
                comparemanager.make_file(tbbzipPath,'current')

                #比较两个版本中的文件变化  返回文件名列表
                deferent_list = comparemanager.compare(previous_path,current_path)
                for filename in deferent_list:
                    deferenFile = DeferentFileNameVesion()
                    deferenFile.filename = filename
                    deferenFile.version = version
                    deferenFile.save()
                    version.is_changefile = True
                    version.save()
            return HttpResponse("{\"status\":\"already_check\"}", content_type='application/json')
        else:
            print('[+]:已经检测完修改文件')
            return HttpResponse("{\"status\":\"already_check\"}", content_type='application/json')

#修改机器到指定的版本
class ChangeMachineToViesionView(View):
    def get(self,request,machine_sn):
        edition_sn = request.GET.get('edition_sn','')
        if edition_sn:
            version = Version.objects.get(edition_sn=edition_sn)
            file_path = version.file
            filname = version.name
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
            source_path = os.path.join(MEDIA_ROOT, str(file_path))
            file = open(source_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filname)
            return response
        else:
            return HttpResponse("{\"status\":\"edition_none\"}", content_type='application/json')




