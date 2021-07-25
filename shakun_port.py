from io import DEFAULT_BUFFER_SIZE
import socket
from sys import getrefcount
import threading
from optparse import Option, OptionParser
from typing_extensions import ParamSpecArgs
from colorama import Fore as F , init
init(autoreset=True)
class main : 
    def __init__(self) -> None:
        self.s = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
        self.green = F.GREEN
        self.red = F.RED
        self.yellow = F.YELLOW
        self.blue = F.BLUE
        self.light = F.LIGHTBLUE_EX
    def shut(self):
        global range_0 , range_1 , ip , portn
        paser = OptionParser(f'''
        {self.green}
                                        __..--.._
             .....              .--~  .....  `.
             .":    "`-..  .    .' ..-'"    :". `
             ` `._ ` _.'`"(     `-"'`._ ' _.' '
                 ~~~      `.          ~~~
                         .'
                         /
                         (
                         ^---'
                        Shakun8

                    ->HELP MENU<-: 
{self.yellow}
            -p or--port:enter the port as u which u want to scan it
            -r : ranging some port exmpl : 1000-2000
            -t : target ip wich u want to scan it

        ''')
        paser.add_option('-t',dest='ip')
        paser.add_option('-r',dest='range')
        paser.add_option('-p','--port',dest='port')
        (options,args) = paser.parse_args()
        if options.ip and options.range != None : 
            ip = options.ip
            range_0 , range_1 = options.range.split('-')[0] , options.range.split('-')[1]
            self.port()
        elif options.ip and options.port != None : 
            ip = options.ip
            portn = options.port    
            self.scan_sp_port()
        else : 
            print(paser.usage)    

    def port(self):
        try : 
            for x in range(int(range_0),int(range_1)):
                #s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                if self.s.connect_ex((ip,x)) == 0:
                    print(self.green + 'Man :)) This is a  Open port : {}'.format(str(x)))
                else : 
                    print(self.red + 'Shut :(( isn"t open port : {}'.format(str(x)))
        except Exception as o  :
            print(o) 

    def scan_sp_port(self):
        try : 
            s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            if self.s.connect_ex((ip,int(portn))) == 0:
                print(self.green + 'Man :)) This is a  Open port : {}'.format(portn))
            else : 
                print(self.red + 'Shut :(( isn"t open port : {}'.format(portn))
        except Exception as ex  :
            print(str(ex))

if __name__ == '__main__':
    run = main()
    run.shut()
