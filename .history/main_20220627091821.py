from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'

app = Flask(__name__)

# 浏览器实例
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--incognito')#无痕模式
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--no-default-browser-check")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
mobileEmulation = {'deviceName': 'iPhone X'}#模拟手机
options.add_experimental_option('mobileEmulation', mobileEmulation)


driver = webdriver.Chrome(chrome_options=options, desired_capabilities = None)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": '''
  Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }
window.navigator.chrome = { runtime: {},  }; }
Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }
  '''
})
    


@app.route('/')
def main():
    return 'Hello World'

@app.route('/play/list')
def playList():
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

    driver.find_element_by_link_text("设置")

    return driver.find_element(By.ID, 'wrapper')
    
    # print(driver.page_source)

    

if __name__ == '__main__':
    app.run()