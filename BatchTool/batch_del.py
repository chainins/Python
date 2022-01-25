# This code help delete all comments in python. Be careful!
# Notice it will delete the code ''' and # in quotes also. I will fix it soon.
# Have fun!
import os
import re
import shutil
import sys
ROOT_DIR = "./testbatch"
def func_dir(func, dirname, ext='.py'):
    pass
class BatchDir:
    def __init__(self,path):
        self.PATH = path
        self.bak_dir()
    def bak_dir(self):
        self.bak_path = self.PATH + '_bak'
        isExist = os.path.exists(self.bak_path)
        if not isExist:
          try:
              shutil.copytree(self.PATH, self.bak_path) 
              print(f'The backup directory {self.bak_path} is created!\n\n' + '-'*30)
          except:
              print('Warning: Backup failed : ' + self.bak_path + ' Execution Stoped.')
              sys.exit()
        else:
          print(f'The backup directory {self.bak_path} has been created before!\n\n' + '-'*30)
    def run_dir(self,func,path,level=0): 
        for originalfile in os.listdir(path):
                filename = os.path.join(path, originalfile)           
                if (os.path.isfile(filename)):   
                    result = func(filename,level)
                    if result:
                        print(' '* level*3 + originalfile + ' settled.' )
                    else:
                        print(' '* level*3 + '----- Warning: Failed to deal with ' + originalfile)
                    pass
                elif (os.path.isdir(filename)):
                    print(' '* level*3 + '+dir: '+originalfile)
                    self.run_dir(func,filename,level + 1)
                    pass
    def deal_file(self,filename,level):
        print(' '* level*3 + '---file--- ' +  filename)
        return True
    def backup_file(self,filename,path):
        pass
    def backup_dir(self,path):
        path = path + '_bak'
        isExist = os.path.exists(path)
        if not isExist:
          os.makedirs(path)
          print(f"The backup directory {path} is created!")
class BatchDir_Del(BatchDir):
    def deal_file(self,filename,level):
        if not re.match(r".*?\.(py|ipynb)$",filename):
            print(' '* level*3 + filename + " is ignored.")
            return False
        bak_file = filename + ".bak"
        try:
            os.rename(filename,bak_file)
        except:
            print("bak exception -->" + bak_file)
        fp_src = open(bak_file,'r')
        fp_dst = open(filename,'a+')
        strfile = fp_src.read()
        replacetxt = re.sub(re.compile("", re.DOTALL), '', strfile)  
        replacetxt = re.sub(re.compile('', re.DOTALL), '', replacetxt)  
        replacetxt = re.sub(re.compile("(?<!(['\"]).)
        replacetxt = '\n'.join([line for line in replacetxt.split('\n') if line.strip() != ''])
        fp_dst.write(replacetxt)    
        fp_src.close()
        os.remove(bak_file)
        fp_dst.close()
        return True
bd = BatchDir_Del(ROOT_DIR)
bd.run_dir(bd.deal_file,ROOT_DIR)