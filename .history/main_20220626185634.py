from flask import Flask
from selenium import webdriver
app = Flask(__name__)

# 浏览器实例

@app.route('/')
def main():
    return 'Hello World'

@app.route('/play')
def play():
    driver = webdriver.Chrome()

    result = driver.get("http://www.baidu.com")
    
    return "111"

if __name__ == '__main__':
    app.run()