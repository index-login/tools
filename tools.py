from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

target=''
domains=''
urls=''

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
        choose==choose.strip()
        if choose == "domain":
            pass
        elif choose =="help":
            print(help_mg)
        elif choose == "exit":
            exit()





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

if __name__ == '__main__':
    main()
