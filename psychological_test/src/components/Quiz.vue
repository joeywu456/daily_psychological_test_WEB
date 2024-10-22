<template>
  <div class="quiz">
    <h2>{{ quiz.title }}</h2>
    <div v-for="(question, index) in quiz.questions" :key="question.id">
      <h3>問題 {{ index + 1 }}: {{ question.text }}</h3>
      <div v-for="option in question.options" :key="option.id">
        <input 
          type="radio" 
          :id="option.id" 
          :name="'question' + question.id" 
          :value="option.id"
          v-model="answers[question.id]"
        >
        <label :for="option.id">{{ option.text }}</label>
      </div>
    </div>
    <button @click="submitQuiz">提交</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'QuizComponent',
  data() {
    return {
      quiz: null,
      answers: {}
    }
  },
  mounted() {
    this.fetchQuiz();
  },
  methods: {
    async fetchQuiz() {
      try {
        const response = await axios.get(`http://localhost:3000/api/quiz?id=${this.$route.params.id}`);
        this.quiz = response.data;
      } catch (error) {
        console.error('Error fetching quiz:', error);
      }
    },
    async submitQuiz() {
      try {
        const response = await axios.post('http://localhost:3000/api/result', {
          quizId: this.quiz.id,
          answers: this.answers
        });
        this.$router.push({ name: 'Result', params: { result: response.data } });
      } catch (error) {
        console.error('Error submitting quiz:', error);
      }
    }
  }
}
</script>

