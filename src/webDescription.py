import requests
from bs4 import BeautifulSoup


def get_website_description(url):
    # url = "https://" + url
    # 发送 HTTP 请求
    response = requests.get(url)

    # 确保请求成功
    if response.status_code == 200:
        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser')
        print(soup.prettify())  # 打印格式化后的 HTML 内容

        # 查找 meta 标签中的描述信息
        description_tag = soup.find('meta', attrs={'name': 'description'})

        # 如果找到了描述信息
        if description_tag:
            return description_tag.get('content'), soup.prettify()
            # return soup.prettify()
        else:
            return "未找到网页描述信息",soup.prettify()
    else:
        return f"请求失败，状态码：{response.status_code}", ""


# 示例使用
# url = "https://www.huntington.com.br"
# description, des2 = get_website_description(url)
# print("网页描述：", des2)
