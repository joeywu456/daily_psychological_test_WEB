# Daily Psychological Test Web Application

這是一個基於 Vue 3 和 Flask 的心理測驗網站。用戶可以參加各種有趣的測驗，並分享結果。


## 前端技術

- **Vue 3**: 用於構建用戶界面。
- **Vue Router 4**: 用於管理應用的路由。
- **Axios**: 用於處理 HTTP 請求。

## 後端技術

- **Flask**: 用於處理後端邏輯和 API。
- **Flask-CORS**: 用於解決跨域資源共享問題。

## 文件說明

### 前端文件

1. `psychological_test/src/main.js`
   - 這是 Vue 應用的入口文件。
   - 使用 `createApp` 創建 Vue 應用實例。
   - 導入並使用 Vue Router。

2. `psychological_test/src/App.vue`
   - 這是 Vue 應用的根組件。
   - 包含應用的基本結構和全局樣式。

3. `psychological_test/src/router/index.js`
   - 定義應用的路由配置。
   - 使用 `createRouter` 和 `createWebHistory` 創建路由實例。
   - 定義了首頁、測驗頁和結果頁的路由。

4. `psychological_test/src/components/QuizList.vue`
   - 顯示可用測驗列表的組件。
   - 使用 Axios 從後端獲取測驗數據。
   - 提供開始測驗的功能。

5. `psychological_test/src/components/Quiz.vue`
   - 顯示測驗問題和選項的組件。
   - 使用 Axios 獲取特定測驗的詳細信息。
   - 允許用戶回答問題並提交答案。

6. `psychological_test/src/components/Result.vue`
   - 顯示測驗結果的組件。
   - 提供分享結果和返回首頁的功能。

### 後端文件

7. `backend/app.py`
   - Flask 應用的主文件。
   - 定義 API 端點，處理測驗數據的獲取和結果的計算。

## 安裝指南

### 前端

1. 確保您已經安裝了 Node.js 和 npm。
2. 進入 `psychological_test` 目錄：
   ```bash
   cd psychological_test
   ```
3. 安裝依賴：
   ```bash
   npm install
   ```
4. 啟動開發服務器：
   ```bash
   npm run serve
   ```
   開發服務器將在 `http://localhost:8080` 運行。

### 後端

1. 確保您已經安裝了 Python 和 pip。
2. 進入 `backend` 目錄：
   ```bash
   cd backend
   ```
3. 安裝 Flask 和相關依賴：
   ```bash
   pip install flask flask-cors
   ```
4. 啟動 Flask 服務器：
   ```bash
   python app.py
   ```
   Flask 服務器將在 `http://localhost:5000` 運行。

## 使用指南

1. 打開瀏覽器並訪問 `http://localhost:8080`。
2. 在首頁選擇一個測驗並點擊"開始測驗"。
3. 回答測驗中的所有問題。
4. 提交測驗後，查看結果。
5. 選擇分享結果或返回首頁。

## 貢獻

歡迎提交問題和功能請求。如果您想貢獻代碼，請先 fork 本倉庫，然後提交 pull request。

## 許可

本項目使用 MIT 許可證。詳情請參閱 LICENSE 文件。