import zipfile
import os
import zipstream
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


