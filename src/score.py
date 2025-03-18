import re


# 定义一个评分函数
from constant.keyWords import RELEVANCE, POPULARITY, PROFESSIONALISM
from src.webDescription import get_website_description


def score_website(url, description):
    scores = {
        "relevance": 0,
        "public_awareness": 0,
        "professionalism": 0
    }

    # 相关性评分 (Relevance)
    relevance_keywords = RELEVANCE
    relevance_score = sum([1 for keyword in relevance_keywords if
                           re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE)])
    scores["relevance"] = min(relevance_score * 2, 9)  # 相关性较为重要，给一个权重
    if scores["relevance"] == 0:
        scores["relevance"] = 1

    # 科普性评分 (Public Awareness)
    public_awareness_keywords = POPULARITY
    public_awareness_score = sum([1 for keyword in public_awareness_keywords if
                                  re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE)])
    scores["public_awareness"] = min(public_awareness_score * 2, 9)  # 偏向大众的内容加分
    if scores["public_awareness"] == 0:
        scores["public_awareness"] = 1

    # 专业性评分 (Professionalism)
    professionalism_keywords = PROFESSIONALISM
    professionalism_score = sum([1 for keyword in professionalism_keywords if
                                 re.search(r'\b' + re.escape(keyword) + r'\b', description, re.IGNORECASE)])
    scores["professionalism"] = min(professionalism_score * 3, 9)  # 专业性较为重要，给更高的权重
    if scores["professionalism"] == 0:
        scores["professionalism"] = 1

    # 评分区间，避免总分超过10
    total_score = min(scores["relevance"] + scores["public_awareness"] + scores["professionalism"], 10)


    return scores, total_score


# # 例子：处理一个网站
# website_data = [
#     {"url": "www.icrhb.org", "description": "We provide advanced reproductive health services and medical research."},
#     {"url": "www.ibisreproductivehealth.org",
#      "description": "Ibis Reproductive Health focuses on global reproductive health education and services for women."},
#     {"url": "www.hxbenefit.com", "description": "Mirena IUD and endometrial health treatments."},
#     {"url": "www.huntington.com.br", "description": "We offer treatments for reproductive health."}
# ]
#
# # 打分并输出
# # for website in website_data:
# #     scores, total_score = score_website(website["url"], website["description"])
# #     print(f"Website: {website['url']}")
# #     print(
# #         f"Scores: Relevance = {scores['relevance']}, Public Awareness = {scores['public_awareness']}, Professionalism = {scores['professionalism']}")
# #     print(f"Total Score: {total_score}")
# #     print("--------")
#
# url = website_data[1]["url"]
# print(url)
# des = get_website_description(url)
# scores, total_score = score_website(url, des)
# print(f"Website: {website_data[1]['url']}")
# print(
#     f"Scores: Relevance = {scores['relevance']}, Public Awareness = {scores['public_awareness']}, Professionalism = {scores['professionalism']}")
# print(f"Total Score: {total_score}")
# print("--------")

