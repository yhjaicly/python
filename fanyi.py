import urllib.request
# request是最基本的HTTP请求库，就像是输入一个地址，然后进入到网站的过程
import urllib.parse
# 工具模块，提供URL的处理办法，拆分，解析，合并
import json
# 将获取到的和输入的json进行编码和解码
content = input('需要翻译的内容:')
# 翻译内容

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://fanyi.youdao.com/'
# 有道翻译查询入口
data = {  # 表单数据--数据在打开F12--Network--找name中的文件--点开查看Prview--看是否是你要翻译的结果--然后找Headers中的Form Data
    'i': content,
    'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_CLICKBUTTION',
            'typoResult': 'false'
}

data = urllib.parse.urlencode(data).encode('utf-8')
# 对POST数据进行编码

response = urllib.request.urlopen(url, data)
# 发出POST请求并获取HTTP响应

html = response.read().decode('utf-8')
# 获取网页内容，并进行解码解码

target = json.loads(html)
# json解析

print("\n翻译结果:%s" % target['translateResult'][0][0]['tgt'])  # 这里找到返回的数据
# 输出翻译结果
