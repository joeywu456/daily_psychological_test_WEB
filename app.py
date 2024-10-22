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
            {
                "id": 2,
                "text": "面對困難時，你通常會怎麼做？",
                "options": [
                    {"id": "a", "text": "慢慢思考解決方案（沉穩）"},
                    {"id": "b", "text": "直接行動，不拖延（果斷）"},
                    {"id": "c", "text": "找別人商量，尋求幫助（社交型）"},
                    {"id": "d", "text": "先冷靜下來，再決定怎麼做（理智）"}
                ]
            },
            {
                "id": 3,
                "text": "以下哪種飲料最符合你的喜好？",
                "options": [
                    {"id": "a", "text": "檸檬汁（酸甜、活潑）"},
                    {"id": "b", "text": "椰子汁（清新、天然）"},
                    {"id": "c", "text": "熱咖啡（濃郁、有深度）"},
                    {"id": "d", "text": "果昔（混搭、有創意）"}
                ]
            }
        ],
        "results": [
            {"id": "apple", "text": "蘋果：你是一個溫暖而有耐心的人，總是給人一種可靠和舒適的感覺，跟你相處就像享受一顆甜甜的蘋果一樣美好。"},
            {"id": "lemon", "text": "檸檬：你性格爽朗，直來直往。雖然有些時候會讓人覺得你有點酸，但其實內心很溫暖。"},
            {"id": "coconut", "text": "椰子：你外表堅強但內心柔軟，就像椰子的外殼與果肉一樣。"},
            {"id": "grape", "text": "葡萄：你多才多藝、善於社交，總是能輕鬆融入任何場景。"}
        ]
    },
    {
        "id": 2,
        "title": "你的靈魂動物是什麼？",
        "questions": [
            {
                "id": 1,
                "text": "你覺得自己更喜歡哪種生活方式？",
                "options": [
                    {"id": "a", "text": "規律的日常（安定）"},
                    {"id": "b", "text": "不斷挑戰新事物（冒險）"},
                    {"id": "c", "text": "舒服自在就好（慵懶）"},
                    {"id": "d", "text": "與朋友一起共度時光（群體）"}
                ]
            },
            {
                "id": 2,
                "text": "你和新認識的人相處時，通常是？",
                "options": [
                    {"id": "a", "text": "觀察對方，慢慢了解（謹慎）"},
                    {"id": "b", "text": "主動找話題聊天（外向）"},
                    {"id": "c", "text": "靜靜待著，感覺合適再互動（被動）"},
                    {"id": "d", "text": "直接問對方興趣（開朗）"}
                ]
            },
            {
                "id": 3,
                "text": "你喜歡哪種自然景觀？",
                "options": [
                    {"id": "a", "text": "廣闊的草原（自由）"},
                    {"id": "b", "text": "茂密的森林（神秘）"},
                    {"id": "c", "text": "美麗的海灘（放鬆）"},
                    {"id": "d", "text": "高聳的山脈（挑戰）"}
                ]
            }
        ],
        "results": [
            {"id": "lion", "text": "獅子：你天生領袖特質，總是能帶動周圍的人，勇敢且有自信。"},
            {"id": "owl", "text": "貓頭鷹：你是一個充滿智慧的人，喜歡安靜的環境，善於觀察細節。"},
            {"id": "dolphin", "text": "海豚：你充滿好奇心，活潑開朗，善於與人溝通，是團體中的開心果。"},
            {"id": "panda", "text": "熊貓：你有一顆柔軟的心，喜歡舒適而悠閒的生活，給人一種非常可愛的感覺。"}
        ]
    },
    {
        "id": 3,
        "title": "你最適合的職業是什麼？",
        "questions": [
            {
                "id": 1,
                "text": "當你面臨一個複雜的問題時，你會怎麼做？",
                "options": [
                    {"id": "a", "text": "把它分成幾個小問題來解決（分析型）"},
                    {"id": "b", "text": "直接著手解決，行動最重要（實踐型）"},
                    {"id": "c", "text": "和朋友討論找靈感（創意型）"},
                    {"id": "d", "text": "仔細查資料，了解所有細節（學術型）"}
                ]
            },
            {
                "id": 2,
                "text": "你更喜歡哪種工作環境？",
                "options": [
                    {"id": "a", "text": "安靜且有規律（穩定）"},
                    {"id": "b", "text": "充滿挑戰和變化（多變）"},
                    {"id": "c", "text": "和很多人一起工作（社交型）"},
                    {"id": "d", "text": "需要不斷創新和想像力（創造型）"}
                ]
            },
            {
                "id": 3,
                "text": "你在團體中通常扮演什麼角色？",
                "options": [
                    {"id": "a", "text": "組織者（負責掌控全局）"},
                    {"id": "b", "text": "行動者（帶動大家向前）"},
                    {"id": "c", "text": "支持者（為大家提供協助）"},
                    {"id": "d", "text": "創意發想者（提出新點子）"}
                ]
            }
        ],
        "results": [
            {"id": "teacher", "text": "教師：你有耐心和責任感，喜歡與人分享知識，是一個很好的教育者。"},
            {"id": "entrepreneur", "text": "企業家：你善於抓住機會，行動力強，適合不斷挑戰的新事物。"},
            {"id": "artist", "text": "藝術家：你富有創意，喜歡表達自我，適合自由而富有靈感的工作。"},
            {"id": "scientist", "text": "科學家：你對細節有極高的敏感度，擅長分析和探索，是探索未知的最佳人選。"}
        ]
    }
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
