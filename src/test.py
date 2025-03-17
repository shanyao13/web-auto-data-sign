from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

# 1 初始化浏览器
driver = webdriver.Chrome()

# 2 打开登陆界面
# driver.get("https://www.baidu.com/")
driver.get("http://221.228.10.206:8002/domains")

print("启动浏览器")

# 3. 设置 Cookie（用你提供的 cookie 内容替换）
cookie = {
    'name': 'user',
    'value': '{"id":106,"username":"ObstetricsReproductiveMedicine","password":"zj6784","subject_code":"ObstetricsReproductiveMedicine"}',
    'domain': '221.228.10.206'
}
driver.add_cookie(cookie)


# 4. 刷新页面，模拟已经登录状态
driver.refresh()
sleep(3)

data = {
    "domainId": 287688,
    "relevance": 9,
    "popularity": 7,
    "professionalism": 8,
    "remark": ""
}
response = session.post(url, json=data)



# 6. 查找并点击标注状态为“未标注”的元素
# 假设 "未标注" 状态的按钮或文本包含在 class="未标注" 或是某个特定元素中
try:
    # 定位到“未标注”的元素，假设它是一个包含文本的按钮或标签
    unmarked_elements = driver.find_elements(By.XPATH, "//td[contains(text(), '未标注')]")

    if unmarked_elements:
        # 获取第一个“未标注”项并点击
        unmarked_elements[0].click()
        print("点击了未标注项")
    else:
        print("未找到未标注项")
except Exception as e:
    print(f"发生错误: {e}")

# 等待点击后的页面更新
sleep(2)

# # 等待搜索框可见并输入
# search_box = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.ID, 'kw'))
# )
# print("输入： 小那同学")
# search_box.send_keys('小那同学')
#
# # 等待搜索按钮可点击并点击
# print("点击搜索")
# search_button = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'su'))
# )
# search_button.click()

# 等待搜索结果加载
sleep(3)

# 关闭浏览器
# driver.close()