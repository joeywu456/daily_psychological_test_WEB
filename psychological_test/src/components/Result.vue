<template>
  <div class="result">
    <h2>測驗結果</h2>
    <p>{{ result.text }}</p>
    <button @click="shareResult">分享結果</button>
    <button @click="backToHome">返回首頁</button>
  </div>
</template>

<script>
export default {
  name: 'ResultComponent', // 修改為多字名稱
  data() {
    return {
      result: this.$route.params.result
    }
  },
  methods: {
    shareResult() {
      // 實現分享功能
      alert('分享功能待實現');
    },
    backToHome() {
      this.$router.push({ name: 'Home' });
    }
  }
}
</script>
