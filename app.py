from flask import Flask, render_template

app = Flask(__name__)

notes = [
    {
        "title": "Python 基础语法",
        "content": "变量、数据类型、输入输出、条件判断、循环"
    },
    {
        "title": "列表与字典",
        "content": "list、dict、tuple、set 的使用方式"
    },
    {
        "title": "函数",
        "content": "函数定义、参数、返回值、lambda 表达式"
    },
    {
        "title": "面向对象",
        "content": "类、对象、继承、多态、封装"
    },
    {
        "title": "Flask Web 开发",
        "content": "路由、模板、静态文件、部署"
    }
]

@app.route('/')
def home():
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
