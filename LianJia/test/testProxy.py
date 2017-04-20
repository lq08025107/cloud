# -*-coding: utf-8 -*-
import requests
import json
r = requests.get('http://112.74.44.61:8000/?types=0&count=5&country=国内')
print r.text
ip_ports = json.loads(r.text)
print ip_ports
ip = ip_ports[0][0]
port = ip_ports[0][1]
proxies = {
    'http':'http://%s:%s'%(ip,port),
    'https':'http://%s:%s'%(ip,port)
}
r = requests.get('http://iliuqiang.net',proxies=proxies)
r.encoding='utf-8'
print r.text