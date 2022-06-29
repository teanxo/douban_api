### 豆瓣数据抓取

> 包含列表基础信息、详情页信息(包含播放源数据)

1. 根据关键词进行抓取豆瓣列表页数据
2. 根据豆瓣链接抓取豆瓣详情

使用教程
```python
    # 安装flask
    pip install flask
    # 安装selenium
    pip install selenium

    python main.py
```


>访问

    http://localhost:5000


接口API
- 列表页：/play/list?title=影视名称&page=当前页数
- 详情页：/play/detail?d=列表页返回的detail_url或影视详情页链接

只供学习参考，请勿商业使用！！