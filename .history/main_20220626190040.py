from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# 浏览器实例

@app.route('/')
def main():
    return 'Hello World'

@app.route('/play')
def play():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    

    result = driver.get("http://www.baidu.com")
    
    return result

if __name__ == '__main__':
    app.run()