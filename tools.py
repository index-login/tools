import asyncio


from asyncio import Queue
from typing import Any
from prompt_toolkit.eventloop import get_event_loop
import prompt_toolkit.application
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.layout import Layout
from prompt_toolkit.widgets import TextArea,Frame,SearchToolbar
from prompt_toolkit.layout.containers import HSplit,VSplit,Window
from prompt_toolkit import Application
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.document import Document
from prompt_toolkit.application.current import get_app
import os
import subprocess
import db

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
ofl_path="/root/tools/OneForAll/oneforall.py"
optionsheight=4

class sub:
    def __init__(self,domain):
        self.domain=domain




# def oneforall(ym):
#     oneforal=["python3", ofl_path, "--target",ym,"--fmt","json","--path",the,"run"]
#     try:
#         all=subprocess.Popen(oneforal,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#     except BaseException:
#         print("oneforall模块出错")
#         all.kill()
    # if all.wait()==0:
    #     print("运行完成!")
        #     print(all.communicate())
    # js=the+"sub_"+ym+".json"
    # subcmd=["subfinder","-d",ym,"-silent","-all"]
    # ssub=subprocess.Popen(subcmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #
    #
    # httpcmd=["httpx","-json","-o",js,"-ports","80,443,8000,8080,8443"]
    # httpx=subprocess.Popen(httpcmd,stdin=ssub.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #
    #
    # amasstxt=the+"amass_"+ym+".txt"
    # amasscmd=['amass','enum','-o',amasstxt,'-d',ym]
    # amass=subprocess.Popen(amasscmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #
    #
    # cattxt_cmd=['cat',amasstxt]
    # amassjson=the+"amass_"+ym+".json"
    # if amass.wait()==0:
    #     cat_txt=subprocess.Popen(cattxt_cmd,stdout=subprocess.PIPE)
    #     httpcmd1 = ["httpx", "-json", "-o", amassjson, "-ports", "80,443,8000,8080,8443"]
    #     subprocess.Popen(httpcmd1, stdin=cat_txt.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # if all.wait() == 0 :
    #     print("完成!")
    #     shu=db.Ato(domain=ym)
    #     return shu

# def xray():
#     html = datetime.now().strftime('%m%d_%H%M')
#     out_html=the+html+".html"
#     xray_cmd=['/root/crawlergo_linux_amd64/xray_linux_amd64','webscan','--listen','127.0.0.1:7777','--html-output',out_html]
#     try:
#         xrayl = subprocess.Popen(xray_cmd,stdout=subprocess.PIPE)
#     except:
#         print("xray报错")
#     return xrayl
async def amass(domain:str):
    ofl_cmd="amass enum -passive -d %s -src" % (domain)
    # print(ofl_cmd)
    pro=await asyncio.subprocess.create_subprocess_shell(ofl_cmd,stderr=asyncio.subprocess.PIPE,stdout=asyncio.subprocess.PIPE)
    L=await pro.wait()
    return True

def findjs():

    pass
def fuzz():

    pass
def arjun():
    pass

def crawlergo():
    pass






def tu() -> str:
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
    return hello




kb=KeyBindings()
@kb.add("c-c",eager=True)
def _(event):
    """

    退出程序
    """

    event.app.exit()


#命令行的修饰
def show_line(buf,buf1):
    return ">>"




# async def create_task():
#
#     return [asyncio.create_task()]

def exec_cmd(cmdstring:str):
    """
    可运行的命令,处理
    """

    # queue = asyncio.Queue(maxsize=10)
    cmdstring=cmdstring.split()

    text=""
    if  "help" == cmdstring[0]:
        text=help_mg
    elif "domain" ==cmdstring[0]:
        text="\n==========\n开始收集%s的域名 ！\n" % cmdstring[1]
        queue.put_nowait(str(cmdstring[1]))
    elif "res" ==cmdstring[0]:
        pass
    elif "db" ==cmdstring[0]:
        a = db.Ato(domain="tuhu.org")
        text=a.show()
    else:
        text="[*]无效命令!\n"
    out_text(text)



def comm_handle(buff):
    """

    接收行的命令，进行处理

    :param buff:
    :return:None
    """
    if buff.text:
        cmdstring=buff.text
        exec_cmd(cmdstring)


#输入窗口
left = TextArea(
    get_line_prefix=show_line,
    completer=cmdcompleter,
    accept_handler=comm_handle,
    multiline=False,
    )

#进行修饰left的边框
commFrame=Frame(left,title="==========mytoolbox==========")


list = TextArea(
    height=optionsheight
)
listFrame=Frame(list,title="属性")


#左边命令结果输出
out = TextArea(read_only=True,wrap_lines=False,scrollbar=True,focus_on_click=True)
#修饰out的边框
outFrame=Frame(out,title="Out")

def out_text(text:str)->None:

    out.text+=text
    # 更新out的光标位置
    out.buffer.cursor_position += len(out.text)

#数据流
dateout = TextArea(
)
#修饰dataout的边框
dateoutFrame=Frame(dateout,title="dataOut")


#右边框分布
rightFrame = HSplit(
    [listFrame,
#Window(height=1,char="="),
    dateoutFrame,]
)

#下部分
body=VSplit(
    [outFrame,
#Window(width=1,char="|*|"),
    rightFrame,]

)

#整个shell主体
root=HSplit([
    commFrame,
    body,
])

root_con: Layout=Layout(root)
queue: Queue[Any]=asyncio.Queue()
async def app_main():

    app = Application(
        layout=root_con,

        full_screen=True,
        key_bindings=kb
    )
    await app.run_async()
# async def res():
#     await asyncio.gather()
#     out.text+=await queue.get()
async def tool_run():
    while True:
        temp=await queue.get()
        L=await amass(temp)
        out.text+="收集完成！"

asyncio.get_event_loop().run_until_complete(asyncio.gather(app_main(),tool_run()))
    # asyncio.run(amass("www.baidu.com"))