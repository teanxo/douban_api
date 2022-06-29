from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# 浏览器实例
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)

@app.route('/')
def main():
    return 'Hello World'

@app.route('/play/list')
def playList():
    title = request.args['title']
    # 默认类目
    cat = '1002'
    # 当前页数
    page = request.args['page']
    # 每页显示条数
    pageSize = 10

    start = (int(page) - 1) * pageSize 
    host = "https://movie.douban.com/subject_search?search_text="+title+"&cat="+str(cat)+"&start="+str(start)
    # 开始请求
    driver.get(host)

    
    return driver.page_source

if __name__ == '__main__':
    app.run()