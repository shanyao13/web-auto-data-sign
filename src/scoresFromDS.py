import null as null
import requests
import json

from constant.dsApiKey import API_KEY
from src.strToJson import strToJson


def getScoresFromDS(domains):
    api_key = API_KEY
    # API 请求的URL
    api_url = "https://api.deepseek.com/chat/completions"

    # 定义请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # 定义请求体
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"Evaluate the relevance, popularity, and professionalism of the following websites in the field of Obstetrics and Reproductive Medicine. "
                        f"Return a score from 0 to 10 for each factor. The output must be formatted as a JSON array of objects, where each object has an 'id' field "
                        f"(corresponding to the website's ID from the provided list) and a 'score' field (a list of three integers representing relevance, popularity, and professionalism). "
                        f"Input Websites: {domains}."
                        f"Example output format: [{{\"id\": 287069, \"score\": [5, 8, 6]}}, {{\"id\": 287070, \"score\": [5, 8, 5]}}]. "

             }
        ],
        "stream": False
    }

    # 发送API请求
    response = requests.post(api_url, headers=headers, data=json.dumps(payload))

    # 解析返回的JSON响应
    if response.status_code == 200:
        result = response.json()
        # 提取助手返回的评分内容
        scores = result.get("choices", [{}])[0].get("message", {}).get("content", "")

        return scores
    else:
        return f"Error: {response.status_code}, {response.text}"

#
# # 示例用法
# domains = {"domains":[{"id":287023,"domain":"zju.womanhospital.cn","subject_code":"ObstetricsReproductiveMedicine","url":"https://zju.womanhospital.cn/index","relevance":0,"popularity":0,"professionalism":0,"remark":"网页无法打开，通过提示可打开新网页，新网页地址（需补充）","updated_at":"2025-03-17 03:12:04"},{"id":287024,"domain":"zivafertility.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://zivafertility.com/fertility","relevance":3,"popularity":9,"professionalism":5,"remark":null,"updated_at":"2025-03-13 05:50:25"},{"id":287025,"domain":"yinstill.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://yinstill.com/testimonials","relevance":2,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:15:53"},{"id":287026,"domain":"www1.nichd.nih.gov","subject_code":"ObstetricsReproductiveMedicine","url":"https://www1.nichd.nih.gov/ncmhep","relevance":3,"popularity":9,"professionalism":9,"remark":null,"updated_at":"2025-03-13 06:16:47"},
#                       {"id":287054,"domain":"www.womenandinfants.org","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.womenandinfants.org/Physicians","relevance":7,"popularity":8,"professionalism":8,"remark":null,"updated_at":"2025-03-13 06:29:14"},{"id":287055,"domain":"www.womed.at","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.womed.at/en","relevance":7,"popularity":8,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:29:47"},{"id":287056,"domain":"www.wmcdothan.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.wmcdothan.com/blog","relevance":7,"popularity":8,"professionalism":7,"remark":null,"updated_at":"2025-03-13 06:29:55"},{"id":287057,"domain":"www.wjgnet.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.wjgnet.com/2218-6220","relevance":6,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:30:03"},{"id":287058,"domain":"www.wisconsinurology.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.wisconsinurology.com/our-services","relevance":6,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:30:12"},{"id":287059,"domain":"www.winfertility.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.winfertility.com/blog","relevance":7,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:30:19"},{"id":287060,"domain":"www.wildemeersch.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.wildemeersch.com/research","relevance":5,"popularity":7,"professionalism":5,"remark":null,"updated_at":"2025-03-13 06:30:27"},{"id":287061,"domain":"www.wildemeersch.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.wildemeersch.com/products","relevance":6,"popularity":7,"professionalism":5,"remark":null,"updated_at":"2025-03-13 06:30:36"},{"id":287062,"domain":"www.whmg.net","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.whmg.net/infertility","relevance":6,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:32:58"},{"id":287063,"domain":"www.whmcenter.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.whmcenter.com/our-staff","relevance":8,"popularity":8,"professionalism":8,"remark":null,"updated_at":"2025-03-13 06:38:08"},
#                       {"id":287064,"domain":"www.whitelotusclinic.ca","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.whitelotusclinic.ca/blog","relevance":8,"popularity":8,"professionalism":7,"remark":null,"updated_at":"2025-03-13 06:38:14"},{"id":287065,"domain":"www.whcma.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.whcma.com/services","relevance":7,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:38:26"},{"id":287066,"domain":"www.westmorelandobgyn.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.westmorelandobgyn.com/services","relevance":7,"popularity":7,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:38:36"},{"id":287067,"domain":"www.wessexfertility.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.wessexfertility.com/blog","relevance":6,"popularity":8,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:38:55"},{"id":287068,"domain":"www.webshop.demaco.nl","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.webshop.demaco.nl/product","relevance":5,"popularity":7,"professionalism":5,"remark":null,"updated_at":"2025-03-13 06:39:07"},{"id":287069,"domain":"www.webmd.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.webmd.com/sex","relevance":5,"popularity":8,"professionalism":6,"remark":null,"updated_at":"2025-03-13 06:39:14"},{"id":287070,"domain":"www.webmd.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.webmd.com/ovarian-cancer","relevance":5,"popularity":8,"professionalism":5,"remark":null,"updated_at":"2025-03-13 06:39:23"},{"id":287071,"domain":"www.webmd.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.webmd.com/menopause","relevance":5,"popularity":8,"professionalism":5,"remark":null,"updated_at":"2025-03-13 06:39:29"},
#                       {"id":287072,"domain":"www.webmd.com","subject_code":"ObstetricsReproductiveMedicine","url":"https://www.webmd.com/infertility-and-reproduction","relevance":5,"popularity":8,"professionalism":5,"remark":null,"updated_at":"2025-03-13 06:39:48"}],
#            "pagination":{"total":2000,"page":1,"pageSize":50,"totalPages":40},"totalRated":674}
#
# scores = getScoresFromDS(domains)
# print(f"score_json: {scores} 类型: {type(scores)}")  # 打印类型和内容
#
# # 将字符串转换为JSON
# modified_scores = strToJson(scores)
#
# print("modified_scores: {modified_scores}")
# # 遍历scores列表，提取每个字典中的id和score
# for score_json in modified_scores:
#     domain_id = score_json.get("id")  # 提取id
#     score = score_json.get("score")  # 提取score
#
#     # 打印id和score
#     print(f"id: {domain_id}, score: {score}")

