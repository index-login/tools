from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import subprocess
import db

#import huepy

#git reset --hard
#git pull
cmdcompleter=WordCompleter(['help','domain','proxy','xray','all','exit'])
help_mg="""
domain  域名收集类
proxy   开启代理
xray    调用xray
exit    退出
all     随便什么url
"""

the=os.getcwd()+"/tmp/"
def main():
    tu()
    while True:
        choose=prompt('mytool>',
            completer=cmdcompleter,
        )
        cmd=choose.split()[0]
        arg=choose.split()[1]
        if cmd == "domain":
            oneforall(arg)
            subfinder(arg)
            db.Ato(domain=arg)
        elif cmd =="help":
            print(help_mg)
        elif cmd == "exit":
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
    oneforal=["python3", "/root/OneForAll/oneforall.py", "--target",ym,"--fmt","json","--path",the,"run"]
    try:
        all=subprocess.Popen(oneforal,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except BaseException:
        print("oneforall模块出错")
        all.kill()
    # if all.wait()==0:
    #     print("运行完成!")
        #     print(all.communicate())
def subfinder(ym):
    js=the+"sub_"+ym+".json"
    subcmd=["subfinder","-d",ym,"-silent","-all"]
    ssub=subprocess.Popen(subcmd,stdout=subprocess.PIPE)
    httpcmd=["httpx","-json","-o",js,"-ports","80,443,8000,8080,8443"]
    httpx=subprocess.Popen(httpcmd,stdin=ssub.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)





if __name__ == '__main__':
    main()
