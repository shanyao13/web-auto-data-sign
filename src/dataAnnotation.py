from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# 1. 启动 WebDriver
driver = webdriver.Chrome()  
driver.get("http://221.228.10.206:8002/domains")  # 替换成实际数据标注网站 URL

while True:
    try:
        # 2. 获取当前域名
        domain_element = driver.find_element(By.CSS_SELECTOR, "#domain")
        domain_name = domain_element.text.strip()
        print(f"当前标注域名: {domain_name}")

        # 3. 判断医药相关性（这里可以改成更复杂的判断逻辑）
        # related = check_medical_relevance(domain_name)  # 需要自定义的函数
        related = 2  # 需要自定义的函数


        # 4. 选择评分（CSS 选择器需要根据实际网站调整）
        select_related = Select(driver.find_element(By.CSS_SELECTOR, "#related-score"))
        select_science = Select(driver.find_element(By.CSS_SELECTOR, "#science-score"))
        select_professional = Select(driver.find_element(By.CSS_SELECTOR, "#professional-score"))

        # 假设使用 0-10 评分，这里可以基于 domain_name 或相关性进行更复杂的策略
        select_related.select_by_value("8" if related else "2")
        select_science.select_by_value("6" if related else "3")
        select_professional.select_by_value("7" if related else "4")

        # 5. 点击提交
        submit_button = driver.find_element(By.CSS_SELECTOR, "#submit-button")
        submit_button.click()
        time.sleep(1)  # 等待提交完成

        # # 6. 进入下一题
        # next_button = driver.find_element(By.CSS_SELECTOR, "#next-button")
        # if next_button.is_enabled():
        #     next_button.click()
        # else:
        #     break  # 没有下一题则退出

        time.sleep(1)  # 避免操作过快

    except Exception as e:
        print("出错:", e)
        break

# 7. 关闭浏览器
driver.quit()

