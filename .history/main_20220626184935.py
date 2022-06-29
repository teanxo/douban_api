from flask import Flask
from selenium import webdriver
app = Flask(__name__)

# 浏览器实例
driver = None

@app.route('/')
def main():
    return 'Hello World'

@app.route('/play')
def play():
    result = driver.get("http://www.baidu.com")
    
    return result

if __name__ == '__main__':
    driver = webdriver.Chrome()
    app.run()