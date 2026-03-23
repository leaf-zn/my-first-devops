from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# 定义一个 Prometheus 计数器，记录请求次数
REQUEST_COUNT = Counter('app_requests_total', 'Total app HTTP requests')

@app.route('/')
def hello():
    REQUEST_COUNT.inc() # 每次访问，计数器加 1
    return "Hello, DevOps World! V1.0"

@app.route('/metrics')
def metrics():
    # 暴露给 Prometheus 或其他 Agent 抓取的指标接口
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)