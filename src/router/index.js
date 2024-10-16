import Vue from 'vue'
import VueRouter from 'vue-router'
import QuizList from '../components/QuizList.vue'
import Quiz from '../components/Quiz.vue'
import Result from '../components/Result.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: QuizList
  },
  {
    path: '/quiz/:id',
    name: 'Quiz',
    component: Quiz
  },
  {
    path: '/result',
    name: 'Result',
    component: Result
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
