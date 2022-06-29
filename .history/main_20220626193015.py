from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# 浏览器实例
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument("start-maximized")
options.add_argument('disable-infobars')

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(chrome_options=options, desired_capabilities = None)
    
title = "奇迹笨小孩"
# 默认类目
cat = '1002'
# 当前页数
page = 1
# 每页显示条数
pageSize = 10

start = (int(page) - 1) * pageSize 
host = "https://movie.douban.com/subject_search?search_text="+title+"&cat="+str(cat)+"&start="+str(start)
# 开始请求
driver.get(host)

print(driver.page_source)

# @app.route('/')
# def main():
#     return 'Hello World'

# @app.route('/play/list')
# def playList():
    

    
#     return driver.page_source

# if __name__ == '__main__':
#     app.run()