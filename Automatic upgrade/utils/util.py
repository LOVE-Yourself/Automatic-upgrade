import zipfile,zipstream,os,shutil,hashlib

from Lyonline.settings import MEDIA_ROOT

class ZipUtilities:
    zip_file = None
    def __init__(self):
        self.zip_file = zipstream.ZipFile(mode='w', compression=zipstream.ZIP_DEFLATED)

    def toZip(self, file, name):
        if os.path.isfile(file):
            self.zip_file.write(file, arcname=os.path.basename(file))
        else:
            self.addFolderToZip(file, name)

    def addFolderToZip(self,folder, name):
        for file in os.listdir(folder):
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                self.zip_file.write(full_path, arcname=os.path.join(name, os.path.basename(full_path)))
            elif os.path.isdir(full_path):
                self.addFolderToZip(full_path, os.path.join(name, os.path.basename(full_path)))

    def close(self):
        if self.zip_file:
            self.zip_file.close()


class Zipfolder:
    def rm_zip(self,startdir):
        if os.path.exists(startdir):
            os.remove(startdir)

    def zip_ya(self,startdir):
        # startdir要压缩的文件夹路径
        file_news = startdir + '.zip'  # 压缩后文件夹的名字
        z = zipfile.ZipFile(file_news, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(startdir):
            fpath = dirpath.replace(startdir, '')  # 不replace的话，就从根目录开始复制
            fpath = fpath and fpath + os.sep or ''  # 实现当前文件夹以及包含的所有文件的压缩
            for filename in filenames:
                z.write(os.path.join(dirpath, filename), fpath + filename)
        z.close()
        print('压缩成功')

    def rm_file(self,startdir):
        for i in os.listdir(startdir):
            path_file = os.path.join(startdir, i)
            if os.path.isfile(path_file):
                os.remove(path_file)

    def un_zip(self,file_name):
        zip_file = zipfile.ZipFile(file_name)
        # 判断同名文件夹是否存在，若不存在则创建同名文件夹
        if os.path.isdir(os.path.splitext(file_name)[0]):
            pass
        else:
            os.mkdir(os.path.splitext(file_name)[0])
        for names in zip_file.namelist():
            zip_file.extract(names, os.path.splitext(file_name)[0])
        zip_file.close()


class compareManager:
    def make_file(self,tbbzipPath,filename):
        # 将复制到 media下 再解压
        basepath = os.path.join(MEDIA_ROOT, 'tbbLibs.zip')
        shutil.copy(tbbzipPath, basepath)
        zipfolder = Zipfolder()
        zipfolder.un_zip(basepath)
        # 删除tbbLibs.zip
        os.remove(basepath)
        # 将tbbLibs中 tbbLibs 移动并改为  previous
        basepath1 = os.path.join(MEDIA_ROOT, 'tbbLibs')
        previous = os.path.join(MEDIA_ROOT, filename)
        shutil.move(os.path.join(basepath1, 'tbbLibs'), previous)
        # 删除空文件夹tbbLibs
        shutil.rmtree(basepath1)

    def create_checksum(self,path):
        fp = open(path)
        checksum = hashlib.md5()
        while True:
            buffer = fp.read(8192)
            if not buffer: break
            checksum.update(buffer.encode('utf8'))
        fp.close()
        checksum = checksum.digest()
        return checksum

    def md5_deferent(self,previous_pathName,current_pathName):
        md5_pre = self.create_checksum(previous_pathName)
        md5_cur = self.create_checksum(current_pathName)
        if md5_pre != md5_cur:
            return False
        else:
            #文件没发生更改
            return True

    def compare(self,previous_path,current_path):
        l1 = []
        for path_name in os.listdir(current_path):
            if path_name in os.listdir(previous_path):
                previous_pathName = os.path.join(previous_path,path_name)
                current_pathName = os.path.join(current_path,path_name)
                if not self.md5_deferent(previous_pathName,current_pathName):
                    #文件发生更改
                    l1.append(path_name)
            else:
                l1.append(path_name)
        return l1




