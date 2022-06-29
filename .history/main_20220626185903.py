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
    driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    result = driver.get("http://www.baidu.com")
    
    return "111"

if __name__ == '__main__':
    app.run()