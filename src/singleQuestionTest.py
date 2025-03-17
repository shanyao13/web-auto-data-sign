from time import sleep
from selenium import webdriver
import requests

# 1. 启动浏览器
driver = webdriver.Chrome()

# 2. 打开网页（确保 Selenium 能访问）
driver.get("http://221.228.10.206:8002/domains")
print("启动浏览器")

# 3. 设置 Cookie（网站可能需要先打开 URL，再设置 Cookie）
cookie = {
    'name': 'user',
    'value': '{"id":106,"username":"ObstetricsReproductiveMedicine","password":"zj6784","subject_code":"ObstetricsReproductiveMedicine"}',
    'domain': '221.228.10.206'
}
driver.add_cookie(cookie)

# 4. 刷新页面，确保 Cookie 生效
driver.refresh()
sleep(3)

# 5. 获取 Selenium 中的 Cookies，并转换为 requests 格式
selenium_cookies = driver.get_cookies()
session = requests.Session()

for cookie in selenium_cookies:
    session.cookies.set(cookie['name'], cookie['value'])

# # 6. 发送 POST 请求
# url = "http://221.228.10.206:8002/api/ratings"
# data = {
#     "domainId": 287690,
#     "relevance": 9,
#     "popularity": 7,
#     "professionalism": 8,
#     "remark": ""
# }
#
# response = session.post(url, json=data)
# print("状态码:", response.status_code)
# print("响应内容:", response.text)
#
# sleep(5)
# # 7. 关闭浏览器
# driver.quit()


# 获取页面信息，包括域名domain和url，elevance/popularity/professionalism
url = "http://221.228.10.206:8002/api/domains"
data = {
    "page": 34,
    "pageSize": 20
}
print("-----获取页面信息-----")
response = session.get(url, json = data)
print("状态码:", response.status_code)
print("响应内容:", response.text)




sleep(5)

