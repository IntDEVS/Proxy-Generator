# Proxy Generator | Python

<a href="https://github.com/pandaxyz-xd"><img title="Autor" src="https://img.shields.io/badge/Author-Panda.xyz-blue?style=for-the-badge&logo=github"></a>





<h3 align="center">  👉 Python Code  </h3>

```python
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
```

<h3 align="center">  👉 Config  </h3>

| UserAgents      |
| ------------- |
| Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36     |
| Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0    |
| Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36     |
| Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 |
| Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 |
| Mozilla/4.0 (compatible; MSIE 6.0; Linux i686 ; en) Opera 9.70 |
