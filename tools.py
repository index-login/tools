from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import subprocess



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
        choose==choose.strip().split()
        if choose[0] == "domain":
            oneforall(choose[1])
        elif choose[0] =="help":
            print(help_mg)
        elif choose[0] == "exit":
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
# def get_imput():
def oneforall(ym):
    print(ym)
    oneforal=["python3", "/root/OneForAll/oneforall.py", "--target",ym,"--fmt","json","run"]
    all=subprocess.Popen(oneforal,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print(all.pid)
    while True:
        a=input(">")
        print(all.returncode)
        if a=="l":
            all.kill()
        # if all.wait()==0:
        #     print(all.communicate())
        #     break
def subfinder(ym):
    pass




if __name__ == '__main__':
    main()
