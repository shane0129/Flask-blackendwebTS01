import pymongo
import urllib.parse
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
username = urllib.parse.quote_plus(config.get("mongodb-atlas", "username"))
password = urllib.parse.quote_plus(config.get("mongodb-atlas", "password"))
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@mycluster0.uw0a7xz.mongodb.net/?retryWrites=true&w=majority")
db = client.Flaskweb
collection=db.webdb
print("資料庫連線成功")

from flask import *
app= Flask(__name__,static_folder="static",static_url_path="/")
app.secret_key="yourpassword" # 設定secret密鑰


# 處理路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "nickname" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/signup", methods=["Post"])
def signup():
    # 從前端接收資料
    nickname=request.form["nickname"]
    email=request.form["email"]
    password=request.form["password"]
    # 檢查會員集合中是否有相同 email 的文件資料
    result=collection.find_one({
        "email":email
    })
    if result !=None:
        return redirect("/error?msg=信箱已經被註冊過了")
    # 把資料放進資料庫，完成註冊
    collection.insert_one({
        "nickname":nickname,
        "email":email,
        "password":password
    })
    return render_template("success.html")

@app.route("/signin", methods=["Post"])
def signin():
    # 從前端接收使用者輸入資料
    email=request.form["email"]
    password=request.form["password"]
    # 檢查信箱跟密碼是否正確
    result=collection.find_one({
    "$and":[
        {"email":email},
        {"password":password}
    ]
})
    # 找不到對應的資料，登入失敗，導向錯誤頁面
    if result==None:
        return redirect("/error?msg=帳號或密碼輸入錯誤")
    # 登入成功，在 Session 紀錄會員資訊，導向到會員頁面
    session["nickname"]=result["nickname"]
    return redirect("/member")

@app.route("/signout")
def signout():
    # 移除 Session 中的會員資訊
    del session["nickname"]
    return redirect("/")

# /error?msg=錯誤訊息
@app.route("/error")
def error():
    message=request.args.get("msg","發生錯誤，請聯繫客服!!!")
    return render_template("error.html",message=message)



if __name__ == "__main__":
    app.run()