<template>
  <div class="quiz-list">
    <h2>今日測驗</h2>
    <div v-if="quiz">
      <h3>{{ quiz.title }}</h3>
      <button @click="startQuiz">開始測驗</button>
    </div>
    <div v-else>
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
      quiz: null,
      error: null
    }
  },
  mounted() {
    this.fetchQuiz();
  },
  methods: {
    async fetchQuiz() {
      try {
        const response = await axios.get('http://localhost:5000/api/quiz');
        this.quiz = response.data;
      } catch (error) {
        console.error('Error fetching quiz:', error);
        this.error = '無法加載測驗，請稍後再試。';
      }
    },
    startQuiz() {
      if (this.quiz) {
        this.$router.push({ name: 'Quiz', params: { id: this.quiz.id } });
      }
    }
  }
}
</script>
