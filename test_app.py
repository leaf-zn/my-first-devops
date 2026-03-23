from app import app

def test_hello():
    # 模拟用户访问首页
    response = app.test_client().get('/')
    # 检查两件事：1. 状态码是不是 200 (成功)；2. 网页内容对不对
    assert response.status_code == 200
    assert b"Hello, DevOps World!" in response.data