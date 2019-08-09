import urllib.request
# request是最基本的HTTP请求库，就像是输入一个地址，然后进入到网站的过程
import urllib.parse
# 工具模块，提供URL的处理办法，拆分，解析，合并
import json
# 将获取到的和输入的json进行编码和解码
from tkinter import Tk, Button, Entry, Label, Text, END


class YouDaoFanyi(object):
    def crawl(self, word):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=http://fanyi.youdao.com/'
        # 有道翻译查询入口
        data = {  # 表单数据--数据在打开F12--Network--找name中的文件--点开查看Prview--看是否是你要翻译的结果--然后找Headers中的Form Data
            'i': word,
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

        # print("\n翻译结果:%s" % target['translateResult'][0][0]['tgt'])  # 这里找到返回的数据
        result = target['translateResult'][0][0]['tgt']
        return result


class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = YouDaoFanyi()

        self.window.title("有道爬虫翻译")
        # 设置窗口大小和位置
        self.window.geometry('310x370')
        self.window.minsize(310, 370)
        self.window.maxsize(310, 370)
        # 创建一个文本框
        self.result_text1 = Text(self.window, background='#ccc')
        self.result_text1.place(x=10, y=5, width=285, height=155)
        self.result_text1.bind("<Key-Return>", self.submit1)

        # 创建一个按钮，为按钮添加事件
        self.submit_btn = Button(
            self.window, text=u'自动翻译', command=self.submit)
        self.submit_btn.place(x=170, y=165, width=70, height=25)
        self.submit_btn2 = Button(self.window, text=u'清空', command=self.clean)
        self.submit_btn2.place(x=250, y=165, width=35, height=25)

        # 翻译结果标题
        self.title_label = Label(self.window, text=u'翻译结果:')
        self.title_label.place(x=10, y=165)
        # 翻译结果

        self.result_text = Text(self.window, background='#ccc')
        self.result_text.place(x=10, y=190, width=285, height=165)
        # 回车翻译

    def submit1(self, event):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)

        # print(content)

    def submit(self):
        # 从输入框获取用户输入的值
        content = self.result_text1.get(0.0, END).strip().replace("\n", " ")
        # 把这个值传送给服务器进行翻译

        result = self.fanyi.crawl(content)
        # 将结果显示在窗口中的文本框中

        self.result_text.delete(0.0, END)
        self.result_text.insert(END, result)
        print(content)
    # 清空文本域中的内容

    def clean(self):
        self.result_text1.delete(0.0, END)
        self.result_text.delete(0.0, END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
