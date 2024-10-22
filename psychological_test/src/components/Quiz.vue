<template>
  <div class="quiz-container" v-if="quiz">
    <h1 class="quiz-title">{{ quiz.title }}</h1>
    <div v-for="(question, index) in quiz.questions" :key="question.id" class="question-container">
      <h3 class="question-text">問題 {{ index + 1 }}: {{ question.text }}</h3>
      <div v-for="option in question.options" :key="option.id" class="option-container">
        <input 
          type="radio" 
          :id="question.id + '-' + option.id"
          :name="'question' + question.id" 
          :value="option.id"
          v-model="answers[question.id]"
          class="option-input"
        >
        <label :for="question.id + '-' + option.id" class="option-label">{{ option.text }}</label>
      </div>
    </div>
    <button @click="submitQuiz" :disabled="isSubmitting" class="submit-button">
      {{ isSubmitting ? '提交中...' : '提交' }}
    </button>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
  <div v-else class="loading">
    加載中...
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'QuizComponent',
  data() {
    return {
      quiz: null,
      answers: {},
      isSubmitting: false,
      errorMessage: ''
    }
  },
  async created() {
    try {
      const quizId = this.$route.params.id
      const response = await axios.get(`http://localhost:3000/api/quiz?id=${quizId}`);
      this.quiz = response.data;
      // 初始化 answers 对象
      this.quiz.questions.forEach(question => {
        this.answers[question.id] = null;
      });
    } catch (error) {
      console.error('Error loading quiz:', error)
      this.errorMessage = 'Failed to load quiz. Please try again later.'
    }
  },
  methods: {
    async submitQuiz() {
      this.isSubmitting = true;
      this.errorMessage = '';
      try {
        const response = await axios.post('http://localhost:3000/api/result', {
          quizId: this.quiz.id,
          answers: this.answers
        });
        this.$router.push({ 
          name: 'Result', 
          query: { result: JSON.stringify(response.data) }
        });
      } catch (error) {
        console.error('Error submitting quiz:', error);
        if (error.response && error.response.status === 404) {
          this.errorMessage = 'API endpoint does not exist, please check server configuration.';
        } else {
          this.errorMessage = 'Failed to submit quiz, please try again later.';
        }
      } finally {
        this.isSubmitting = false;
      }
    }
  }
}
</script>

<style scoped>
.quiz-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.quiz-title {
  color: #333;
  font-size: 28px;
  margin-bottom: 20px;
}

.question-container {
  margin-bottom: 30px;
}

.question-text {
  color: #444;
  font-size: 20px;
  margin-bottom: 15px;
}

.option-container {
  margin-bottom: 15px;
  position: relative;
}

.option-input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

.option-label {
  display: block;
  position: relative;
  padding-left: 35px;
  margin-bottom: 12px;
  cursor: pointer;
  font-size: 18px;
  color: #555;
  user-select: none;
  transition: all 0.3s ease;
}

.option-label:before {
  content: '';
  position: absolute;
  left: 0;
  top: 0;
  width: 20px;
  height: 20px;
  border: 2px solid #4CAF50;
  border-radius: 50%;
  background-color: #fff;
  transition: all 0.3s ease;
}

.option-input:checked + .option-label:before {
  background-color: #4CAF50;
}

.option-label:after {
  content: '';
  position: absolute;
  display: none;
  left: 8px;
  top: 8px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: white;
}

.option-input:checked + .option-label:after {
  display: block;
}

.option-input:checked + .option-label {
  color: #4CAF50;
  font-weight: bold;
}

.submit-button {
  background-color: #4CAF50;
  color: white;
  padding: 12px 24px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 18px;
  transition: background-color 0.3s;
  display: block;
  margin: 20px auto 0;
}

.submit-button:hover {
  background-color: #45a049;
}

.submit-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}

.error-message {
  color: #ff0000;
  margin-top: 10px;
  text-align: center;
}

.loading {
  font-size: 20px;
  color: #666;
  text-align: center;
  margin-top: 50px;
}
</style>
