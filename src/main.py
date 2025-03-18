from time import sleep
from selenium import webdriver
import requests

# 1. 启动浏览器
from constant.domainConfig import DOMAINS_IP, DOMAINS_API_IP, RATING_API_IP, USERNAME, PASSWORD, SUBJECT_CODE, DOMAIN
from src.scoresFromDS import getScoresFromDS
from src.strToJson import strToJson

driver = webdriver.Chrome()

# 2. 打开网页（确保 Selenium 能访问）
driver.get(DOMAINS_IP)
print("启动浏览器")

# 3. 设置 Cookie（网站可能需要先打开 URL，再设置 Cookie）
# cookie = {
#     'name': 'user',
#     'value': f'{{"id":106,"username":{USERNAME},"password":{PASSWORD},"subject_code":{SUBJECT_CODE}}}',
#     'domain': '221.228.10.206'
# }
cookie = {
    'name': 'user',
    'value': f'{{"id":106,"username":"{USERNAME}","password":"{PASSWORD}","subject_code":"{SUBJECT_CODE}"}}',
    'domain': DOMAIN
}
driver.add_cookie(cookie)

# 4. 刷新页面，确保 Cookie 生效
driver.refresh()
sleep(1)

# # 5. 获取 Selenium 中的 Cookies，并转换为 requests 格式
selenium_cookies = driver.get_cookies()
session = requests.Session()
#
for cookie in selenium_cookies:
    session.cookies.set(cookie['name'], cookie['value'])


# 获取页面信息，包括域名domain和url，elevance/popularity/professionalism
url = DOMAINS_API_IP
for ipage in range(36,38):
    data = {
        "page": ipage,
        "pageSize": 20
    }
    print("-----获取页面信息-----")
    response = session.get(url, params=data)
    print("状态码:", response.status_code)
    print("响应内容:", response.text)

    # for webInfo in response.text:
    #     des = get_website_description(webInfo["url"])
    response_data = response.json()
    print(response_data)
    #
    #
    domains = response_data["domains"]
    print(domains)
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


    # 2、调用大模型，输入url，返回分数-----------------------------------
    scores = getScoresFromDS(domains)
    modified_scores = strToJson(scores)

    url_rating = RATING_API_IP
    for score_json in modified_scores:
        domain_id = score_json.get("id")  # 提取id
        score = score_json.get("score")  # 提取score
        data = {
            "domainId": domain_id,
            "relevance": score[0],
            "popularity": score[1],
            "professionalism": score[2],
            "remark": ""  # 可根据需要填充备注
        }

        response = session.post(url_rating, json=data)

        if response.status_code == 200:
            print(f"成功提交: domainId={data['domainId']}, 响应: {response.json()}")
        else:
            print(f"提交失败: domainId={data['domainId']}, 状态码: {response.status_code}, 响应: {response.text}")

        sleep(1)

sleep(3)
# 关闭浏览器
driver.quit()  # 关闭浏览器并退出 WebDriver 会话

