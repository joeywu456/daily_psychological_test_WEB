from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # 這將允許所有域的請求

# 模擬數據庫
quizzes = [
    {
        "id": 1,
        "title": "你是哪種水果？",
        "questions": [
            {
                "id": 1,
                "text": "當你和朋友出去玩時，你喜歡的活動是什麼？",
                "options": [
                    {"id": "a", "text": "爬山或戶外活動（較耐性、有毅力）"},
                    {"id": "b", "text": "吃好吃的餐廳（愛享受、有品味）"},
                    {"id": "c", "text": "安靜地看書或聊天（文靜、有深度）"},
                    {"id": "d", "text": "看熱鬧的演唱會或展覽（熱情、活躍）"}
                ]
            },
            # ... 其他問題
        ],
        "results": [
            {"id": "apple", "text": "蘋果：你是一個溫暖而有耐心的人，總是給人一種可靠和舒適的感覺，跟你相處就像享受一顆甜甜的蘋果一樣美好。"},
            {"id": "lemon", "text": "檸檬：你性格爽朗，直來直往。雖然有些時候會讓人覺得你有點酸，但其實內心很溫暖。"},
            {"id": "coconut", "text": "椰子：你外表堅強但內心柔軟，就像椰子的外殼與果肉一樣。"},
            {"id": "grape", "text": "葡萄：你多才多藝、善於社交，總是能輕鬆融入任何場景。"}
        ]
    },
    # ... 其他測驗
]

@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    quiz_id = request.args.get('id', type=int)
    if quiz_id:
        quiz = next((q for q in quizzes if q['id'] == quiz_id), None)
        if quiz:
            return jsonify(quiz)
        else:
            return jsonify({"error": "Quiz not found"}), 404
    else:
        return jsonify(random.choice(quizzes))

@app.route('/api/result', methods=['POST'])
def get_result():
    data = request.json
    quiz_id = data.get('quizId')
    answers = data.get('answers')
    
    quiz = next((q for q in quizzes if q['id'] == quiz_id), None)
    if not quiz:
        return jsonify({"error": "Quiz not found"}), 404
    
    # 這裡應該有更複雜的邏輯來決定結果
    result = random.choice(quiz['results'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
