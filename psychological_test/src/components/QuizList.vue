<template>
  <div class="quiz-list">
    <h2 class="quiz-list-title">今日測驗</h2>
    <div v-if="quiz" class="quiz-card">
      <h3 class="quiz-name">{{ quiz.title }}</h3>
      <button @click="startQuiz" class="start-button">開始測驗</button>
    </div>
    <div v-else class="loading">
      正在加載測驗...
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'QuizList',
  data() {
    return {
      quiz: null
    }
  },
  mounted() {
    this.fetchQuiz();
  },
  methods: {
    async fetchQuiz() {
      try {
        const response = await axios.get('http://localhost:3000/api/quiz');
        this.quiz = response.data;
      } catch (error) {
        console.error('Error fetching quiz:', error);
      }
    },
    startQuiz() {
      this.$router.push({ name: 'Quiz', params: { id: this.quiz.id } });
    }
  }
}
</script>

<style scoped>
.quiz-list {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.quiz-list-title {
  color: #333;
  font-size: 28px;
  margin-bottom: 20px;
  text-align: center;
}

.quiz-card {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}

.quiz-card:hover {
  transform: translateY(-5px);
}

.quiz-name {
  color: #444;
  font-size: 22px;
  margin-bottom: 15px;
}

.start-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  display: block;
  width: 100%;
  max-width: 200px;
  margin: 0 auto;
}

.start-button:hover {
  background-color: #45a049;
}

.loading {
  text-align: center;
  color: #666;
  font-size: 18px;
  margin-top: 20px;
}
</style>
