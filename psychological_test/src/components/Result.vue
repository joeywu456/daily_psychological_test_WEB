<template>
  <div class="result-container" v-if="result">
    <h1 class="result-title">測驗結果</h1>
    <div class="result-content">
      <p>{{ result.text }}</p>
    </div>
    <button @click="goHome" class="home-button">返回首頁</button>
  </div>
  <div class="no-result" v-else>
    <p>沒有找到結果數據。</p>
    <button @click="goHome" class="home-button">返回首頁</button>
  </div>
</template>

<script>
export default {
  name: 'ResultComponent',
  data() {
    return {
      result: null
    }
  },
  created() {
    // Get result from route query
    const resultString = this.$route.query.result;
    if (resultString) {
      try {
        this.result = JSON.parse(resultString);
      } catch (error) {
        console.error('Error parsing result data:', error);
      }
    }
    
    // Log error if result doesn't exist
    if (!this.result) {
      console.error('No result data found');
    }
  },
  methods: {
    goHome() {
      this.$router.push({ name: 'Home' });
    }
  }
}
</script>

<style scoped>
.result-container, .no-result {
  max-width: 800px;
  margin: 0 auto;
  padding: 30px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  text-align: center;
}

.result-title {
  color: #333;
  font-size: 28px;
  margin-bottom: 20px;
}

.result-content {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 5px;
  margin-bottom: 20px;
  font-size: 18px;
  color: #444;
  line-height: 1.6;
}

.home-button {
  background-color: #4CAF50;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.home-button:hover {
  background-color: #45a049;
}

.no-result p {
  color: #666;
  font-size: 18px;
  margin-bottom: 20px;
}
</style>
