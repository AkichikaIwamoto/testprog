# coding: utf-8
from bottle import route,run,get,request

# 初期表示
@route("/test1")
def init():
    return """
    <form action="/display1" method="GET">
    words: <input name="words" type="text" />
    <input value="登録" type="submit" />
    </form>
    """

@route("/display1", method="GET")
def dosp1():
    str_input = request.query.words
    res = ""
    for i in range(len(str_input)):
        res += str_input[i] + "゛"
    return "result -> {}".format(res)

run(host='127.0.0.1', port=8765)