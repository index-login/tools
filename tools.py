from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
import os
import subprocess
import db
from _datetime import datetime
#import huepy

#git reset --hard
#git pull
cmdcompleter=WordCompleter(['help','domain','proxy','xray','all','exit','show','start','stop'])
help_mg="""
domain              域名收集类
proxy               开启代理
xray start/stop     调用xray
exit                退出
all                 随便什么url
show                当前数据
"""

the=os.getcwd()+"/tmp/"
def main():
    x_r_a_y = False
    tu()

    while True:
        if x_r_a_y == False:
            print("xray状态:关闭")
        else:
            print("xray状态:开启")
        choose=prompt('mytool>',
            completer=cmdcompleter,

        )
        choose2=choose
        if choose2 == "":
            continue
        cmd=choose2.split()[0]
        if cmd == "domain":
            if len(choose2.split()) > 1:
                con1,con2=oneforall(choose2.split()[1])
            # subfinder(choose2.split()[1])
            # cmd2=choose2.split()[1]
            # db.Ato(domain=cmd2)
        elif cmd == "help":
            print(help_mg)
        elif cmd == "exit":
            exit()
        elif cmd == "show":
            shu.show()
        elif cmd == "xray":
            if len(choose2.split()) > 1:
                con = choose2.split()[1]
                if con == "stop":
                    xraytu.kill()
                    xraytu.stdout.close()
                    x_r_a_y = False
                elif con == "start":
                    if x_r_a_y == True:
                        print("xray已经打开")
                        continue
                    xraytu=xray()
                    x_r_a_y=True
                else:
                    print("xray命令错误")
        else:
            print("无效命令")
        if con1.poll() == 0:
            if con2.poll()==0:
                shu = db.Ato(domain=ym)
                print("完成！")



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

def main_show():
    pass

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
    js=the+"sub_"+ym+".json"
    subcmd=["subfinder","-d",ym,"-silent","-all"]
    ssub=subprocess.Popen(subcmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    httpcmd=["httpx","-json","-o",js,"-ports","80,443,8000,8080,8443"]
    httpx=subprocess.Popen(httpcmd,stdin=ssub.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    amasstxt=the+"amass_"+ym+".txt"
    amasscmd=['amass','enum','-o',amasstxt,'-d',ym]
    amass=subprocess.Popen(amasscmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    cattxt_cmd=['cat',amasstxt]
    cat_txt=subprocess.Popen(cattxt_cmd,stdout=httpx.stdin)
    # while True:
    #
        # if all.poll() == 0 :
        #     if  amass.poll() == 0:
        #         print("完成!")
        #         shu=db.Ato(domain=ym)
        #         return shu
        #         break
    return all,amass
def xray():
    html = datetime.now().strftime('%m%d_%H%M')
    out_html=the+html+".html"
    xray_cmd=['/root/crawlergo_linux_amd64/xray_linux_amd64','webscan','--listen','127.0.0.1:7777','--html-output',out_html]
    try:
        xrayl = subprocess.Popen(xray_cmd,stdout=subprocess.PIPE)
    except:
        print("xray报错")
    return xrayl

def findjs():
    pass
def fuzz():
    pass
def arjun():
    pass

if __name__ == '__main__':
    main()
