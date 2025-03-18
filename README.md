# web-auto-data-sign
自动化网页数据获取、大模型分析判断和数据标注
# 项目描述
- 项目使用 Python 和 Selenium 自动化技术实现网页数据抓取。
- 调用deepseek接口，完成数据分析，并将分析后的数据按格式要求进行封装。
- 实现自动化数据标注打分工作。
# 安装&使用
1、克隆仓库
```shell
git clone https://github.com/shanyao13/web-auto-data-sign.git
cd web-auto-data-sign
```
2、环境搭建
```shell
python -m venv web-auto
source web-auto/bin/activate  # Mac/Linux
# web-auto\Scripts\activate  # Windows
pip install selenium
```
3、启动程序
```shell
python main.py
```
# 注意事项
- LLM api如deepseek、open ai等，需自行创建api key
- 数据标注网站需自行获取用户名密码等
- 可根据不同场景，调整LLM提示词
- 创建 constant文件夹，内部存储网站、用户等信息
- 安装chrome driver插件
# 许可协议
MIT License
