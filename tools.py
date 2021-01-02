from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import subprocess

#git reset --hard
#git pull

cmdcompleter=WordCompleter(['help','domain','proxy','xray','exit'])
help_mg="""
domain  域名收集类
proxy   开启代理
xray    调用xray
exit    退出
123123`
"""
def main():
    tu()
    while True:
        choose=prompt('mytool>',
            completer=cmdcompleter,
        )
        cmd=choose.split()
        if cmd[0] == "domain":
            oneforall(choose[1])
        elif cmd[0] =="help":
            print(help_mg)
        elif cmd[0] == "exit":
            exit()
        else:
            print("无效命令")


def tu():
    hello="""
       **                      **
  /**                     /**
 ******  ******   ******  /**
///**/  **////** **////** /**
  /**  /**   /**/**   /** /**
  /**  /**   /**/**   /** /**
  //** //****** //******  ***
   //   //////   //////  /// 
    
    """
    print(hello)
def oneforall(ym):
    oneforal=["python3", "/root/OneForAll/oneforall.py", "--target",ym,"--fmt","json","run"]
    try:
        all=subprocess.Popen(oneforal,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except BaseException:
        print("oneforall模块出错")
        all.kill()
    if all.wait()==0:
        print("运行完成!")
        #     print(all.communicate())
def subfinder(ym):
    sub_cmd=[]
    sub=subprocess.Popen()




if __name__ == '__main__':
    main()
