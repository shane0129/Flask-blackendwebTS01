# Flask-blackendwebTS01
Flask 網站後端會員登入系統開發
前端:HTML
後端:Flask
資料庫:Mongodb
部屬:Flyio

前端頁面規劃
1. 前端頁面規劃
1.1 採取使用者的立場思考系統操作流程
1.2 前端頁面最貼近使用者的網站體驗
2. 三個主要頁面
2.1 首頁：用來註冊、登入
2.2 會員頁：提供會員專屬資訊或服務
2.3 錯誤頁：發生錯誤時導向到此頁面

建立會員註冊功能
1. 會員註冊功能規劃
1.1 首頁建立註冊表單
1.2 建立註冊功能路由
1.3 檢查資料庫中的註冊信箱是否重複，並完成註冊

建立會員登入、登出功能
1. 會員登入功能規劃
1.1 首頁建立登入表單
1.2 建立登入功能路由
1.3 檢查資料庫中是否有對應的信箱和密碼，儲存會員資訊在 Session 中，登入成功
2. 會員登出功能規劃
2.1 會員頁建立登出連結
2.2 建立登出功能路由
2.3 移除 Session 中的會員資訊，登出成功
