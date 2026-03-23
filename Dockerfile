# 使用官方的轻量级 Python 环境作为基础
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 把依赖清单复制进去并安装
COPY requirements.txt .
RUN pip install -r requirements.txt

# 把我们写的代码复制进去
COPY . .

# 告诉容器启动时运行什么命令
CMD ["python", "app.py"]