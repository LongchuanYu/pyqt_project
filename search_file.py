
PATH = r'E:\MyDocument\My CharisC3-EFI'  # 要搜索的目录地址

TARGET_PATH = r'E:\MyDocument\新しいフォルダー\1' # 把搜索结果复制到目的地址

NAME_PATH = r'1.txt' # 要读取的文件（同时搜索多个）

# NAME = '333' # 搜索一个

NAMES = ['02.ｻｲｽﾞ混在［同幅］（ｽﾃｰﾌﾟﾙ）'] # 自定义搜索，如果填写了这个字段，则忽略从文件加载

READ_FROM_FILE = 1 #是否开启从文件加载





import os
from shutil import copyfile
class Search():
    def __init__(self):
        self.names = []
        self.func = None
        self.once = True
        self.founded = False
    def __core(self,path,name):
        
        files = os.listdir(path)
        for file in files:
            if os.path.isdir(os.path.join(path,file)):
                self.__core( os.path.join( path,file),name)
            elif name in file:
                self.func(os.path.join(path,file))
                self.founded = True
                if self.once:return
    def searchName(self,path,name,func,once=True):
        self.func = func
        self.once = once
        self.founded = False
        self.__core(path,name)
        if not self.founded:
            print(name + ' 未找到')
    def searchNames(self,path,names,func,once=True):
        if not len(names):
            print("names error.")
            return
        
        self.names = names
        self.func = func
        self.once = once
        not_found_list = []
        for name in names:
            self.founded = False
            self.__core(path,name)
            if not self.founded:
                not_found_list.append(name)
        if len(not_found_list):
            print('以下项目未找到：')
            for item in not_found_list:
                print(item)


def func(path):
    name = path.split('\\')
    tar = os.path.join(TARGET_PATH,name[-1])
    copyfile(path,tar)

def main():
    s = Search()
    # s.searchName(PATH,NAME,func,False)
    if not len(NAMES) and READ_FROM_FILE:
        with open(NAME_PATH,'r',encoding='utf-8') as f:
            for line in f:
                NAMES.append(line.strip('\n'))

    s.searchNames(PATH,NAMES,func,False)
main()