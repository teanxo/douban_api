from sqlite3 import connect
from urllib import response
from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'

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
# mobileEmulation = {'deviceName': 'iPhone X'}#模拟手机
# options.add_experimental_option('mobileEmulation', mobileEmulation)


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

# 获取列表数据
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

    # 查询列表数据
    rep_list = driver.find_element(By.ID, 'wrapper').find_element(By.ID, 'root').find_elements(By.XPATH,'//*[@class="item-root"]')

    list = []    

    for item in rep_list:
      i = {}
      # 详情页跳转链接
      i['detail_url'] = item.find_element(By.CLASS_NAME, 'cover-link').get_attribute('href')
      # 封面
      i['cover_link'] = item.find_element(By.CLASS_NAME, 'cover-link').find_element(By.TAG_NAME, 'img').get_attribute('src')
      # 电影名称
      i['name'] = item.find_element(By.CLASS_NAME, 'detail').find_element(By.CLASS_NAME, 'title').find_element(By.TAG_NAME, 'a').text
      # 评分
      try:
        i['rating'] = item.find_element(By.CLASS_NAME, 'detail').find_element(By.CLASS_NAME, 'rating').find_element(By.CLASS_NAME, 'rating_nums').text
      except:
        print(i['name']+"无评分")
      # 摘要
      i['abstract'] = item.find_element(By.CLASS_NAME, 'detail').find_element(By.CLASS_NAME, 'abstract').text
      # 摘要2
      i['abstract_2'] = item.find_element(By.CLASS_NAME, 'detail').find_element(By.CLASS_NAME, 'abstract_2').text
      list.append(i)

    return {
      "code": 1,
      "data":list
    }


# 获取详情
@app.route('/play/detail')
def playDetail():

  resp = {}

  # 详情页地址
  detail_url = request.args['d']
  
  # 开始请求
  driver.get(detail_url)


  # 获取主容器
  wrap = driver.find_element(By.ID, 'wrapper')

  content = wrap.find_element(By.ID, 'content')


  # 标题
  resp['title'] = content.find_element(By.TAG_NAME, 'h1').text()
  
  # 图片
  resp['pic'] = content.find_element(By.ID, 'mainpic').find_element(By.TAG_NAME, 'img').get_attribute('src')
  # 信息
  handlerInfo(content)
  return resp

def handlerInfo(content):
  info = {}
  infoStr = content.find_element(By.XPATH, '//*[@id="info"]').text()
  print(infoStr)

if __name__ == '__main__':
    app.run()