import urllib.request
import json
from colorama import *

req = urllib.request.Request("http://free-proxy-list.net/")
req.add_header("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.01")
sourcecode = urllib.request.urlopen(req)
part = str(sourcecode.read())
part = part.split("<tbody>")
part = part[1].split("</tbody>")
part = part[0].split("<tr><td>")
lista = ""
for proxy in part:
    proxy = proxy.split("</td><td>")
    try:
        proxylist=proxylist + proxy[0] + ":" + proxy[1] + "\n"
    except:
        pass
out_file = open("[PROXY].txt","w")
out_file.write(lista)
out_file.close()
