import re
import os
import datetime
from dateutil.relativedelta import relativedelta
    
    

class main:       
    def del_line():#删除带有'Toltal number of errors'的行,为写入做准备   
        filename="error.txt"
        list = []
        matchPattern = re.compile(r'Toltal number of errors')#从头打开要读取的文件
        file = open("F:\DESKTOP\log_out\\"+filename,'r')  
        while 1:
            line = file.readline()
            if not line:
                break
            elif matchPattern.search(line):
                pass
            else:
                list.append(line)
        file.close()
        file = open(r"F:\DESKTOP\log_out\error.txt", 'w')#从头打开要读取的文件
        for i in list:
            file.write(i)
        file.close()#删除带有'Toltal number of errors'的行
    
    
    def write(logname):#把含有关键词[fatal error]的行写入error.txt
        f = open("F:\DESKTOP\log\\"+logname+".txt",'r',encoding='utf-8')#从头打开要读取的文件
        w = open("F:\DESKTOP\log_out\error.txt",'a',encoding='utf-8')#从最后一行打开要写入的文件
        lines = f.readlines()  
        for lines in lines:#对TXT 进行逐行读取
           if '[fatal error]' in lines:#如果关键字在行中，则输出这行内容
                print(lines)
                lines=lines.strip('\n')
                w.write(lines)
        w.close()


    def check_write_errors():
        i = open("F:\DESKTOP\log_out\error.txt",'r',encoding='utf-8')#从头打开要读取的文件
        count = len(open("F:\DESKTOP\log_out\error.txt",'r').readlines())
        i.close()#检测error数
        i = open("F:\DESKTOP\log_out\error.txt",'a',encoding='utf-8')#从最后一行打开要写入的文件
        last="\nToltal number of errors:"
        i.write(last)
        count2=str (count)
        i.write(count2)#写入error数
        n="\n" 
        i.write(n)#换行
        i.close()
    
    
    def clean():
        date = datetime.datetime.now().strftime('%Y-%m-%d')#获取年月日
        print(date)
        lastdate =(datetime.datetime.now() + relativedelta(days=-1)).strftime("%Y-%m-%d")#获取上一天年月日
        print(lastdate)
         
        
        
        f=open("F:\DESKTOP\log_out\log_list\\"+lastdate+".txt",'r',encoding='utf-8')#从头打开要读取的文件
        lines = f.readlines() #读取所有行
        last_line = lines[-1] #取最后一行   
        print(last_line)
        last_num=last_line
        f.close() 
            
        
        
        file_path = "F:\DESKTOP\log"
        path_list = os.listdir(file_path) #遍历整个文件夹下的文件name并返回一个列表
        f = open("F:\DESKTOP\log_out\log_list\\"+date+".txt",'w',encoding='utf-8')#从头打开要写入的文件
        f.close()#清空log_list
        path_name = []#定义一个空列表
        
        for i in path_list:
            path_name.append(i.split(".")[0]) #若带有后缀名，利用循环遍历path_list列表，split去掉后缀名
        path_name.sort() #排序
        for file_name in path_name:
            # "a"表示以不覆盖的形式写入到文件中,当前文件夹如果没有"save.txt"会自动创建
            with open("F:\DESKTOP\log_out\log_list\\"+date+".txt",'a',encoding='utf-8') as file:
                file.write(file_name + "\n")
                #print(file_name)
            file.close()
         
            
        
        lines = []
        f=open("F:\DESKTOP\log_out\log_list\\"+date+".txt",'r',encoding='utf-8')#从头打开要读取的文件
        for line in f.readlines()[int(last_num):]:
            lines.append(line)
        w=open("F:\DESKTOP\log_out\log_list\\"+date+"_todo_list.txt",'w',encoding='utf-8')#从头打开要读取的文件
        for line in lines:
                w.write(line)   
        f.close() 



    def main():
        date = datetime.datetime.now().strftime('%Y-%m-%d')#获取年月日
        w=open("F:\DESKTOP\log_out\log_list\\"+date+"_todo_list.txt",'r',encoding='utf-8')#从头打开要读取的文件
        lines=w.readlines()
        for lines in lines:#对TXT 进行逐行读取
            lines=lines.strip('\n')
            main.write(lines)


main.clean()
main.del_line()
main.main()
main.check_write_errors()