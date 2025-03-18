from time import sleep
from selenium import webdriver
import requests

# 1. 启动浏览器
from src.score import score_website
from src.scoresFromDS import getScoresFromDS
from src.webDescription import get_website_description

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
sleep(1)

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
    "page": 35,
    "pageSize": 20
}
print("-----获取页面信息-----")
response = session.get(url, json = data)
print("状态码:", response.status_code)
print("响应内容:", response.text)

# for webInfo in response.text:
#     des = get_website_description(webInfo["url"])
response_data = response.json()
print(response_data)


domain = response_data["domains"]
print(domain)
# test_url = domain["url"]

# # 1、自己写打分逻辑------------------------------------------------判断不准确
# webInfo1, webInfo2 = get_website_description(test_url)
#
# scores1, total_score1 = score_website(test_url, webInfo1)
# scores2, total_score2 = score_website(test_url, webInfo2)
# print(
#     f"Scores1: Relevance = {scores1['relevance']}, Public Awareness = {scores1['public_awareness']}, Professionalism = {scores1['professionalism']}")
# print(f"Total Score1: {total_score1}")
# print("--------")
# print(
#     f"Scores2: Relevance = {scores2['relevance']}, Public Awareness = {scores2['public_awareness']}, Professionalism = {scores2['professionalism']}")
# print(f"Total Score2: {total_score2}")

# # 2、调用大模型，输入url，返回分数-----------------------------------cost money
# scores = getScoresFromDS(test_url)
#
#
# # post 打分
# scores_list = [int(x.strip()) for x in scores.split(",")]
#
# url_rating = "http://221.228.10.206:8002/api/ratings"
# data = {
#     "domainId": 287725,
#     "relevance": scores_list[0],
#     "popularity": scores_list[1],
#     "professionalism": scores_list[2],
#     "remark": ""
# }
#
# response = session.post(url_rating, json=data)
# print("状态码:", response.status_code)
# print("响应内容:", response.text)
#
# sleep(5)







sleep(5)

