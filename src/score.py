import requests
from bs4 import BeautifulSoup


def evaluate_website(url):
    try:
        # 发送请求获取网页内容
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return f"请求失败，状态码: {response.status_code}", 0, 0, 0

        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text().lower()

        # 关键词列表
        keywords_relevance = ["obstetrics", "reproductive", "pregnancy", "gynecology", "fertility", "妇产科", "生殖", "妊娠"]
        keywords_popularity = ["health education", "科普", "常见问题", "健康", "预防", "知识"]
        keywords_professionalism = ["研究", "论文", "专家", "指南", "学术", "医学"]

        # 评分计算函数
        def calculate_score(text, keywords):
            count = sum(text.count(word) for word in keywords)
            return min(10, count)  # 限制最高分为 10

        # 计算评分
        relevance_score = calculate_score(text, keywords_relevance)
        popularity_score = calculate_score(text, keywords_popularity)
        professionalism_score = calculate_score(text, keywords_professionalism)

        return relevance_score, popularity_score, professionalism_score

    except Exception as e:
        return f"请求出错: {str(e)}", 0, 0, 0


# 示例调用
url = "https://zju.womanhospital.cn/index"
scores = evaluate_website(url)
print(f"相关性：{scores[0]}/10")
print(f"科普性：{scores[1]}/10")
print(f"专业性：{scores[2]}/10")
