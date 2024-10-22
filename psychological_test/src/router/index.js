import { createRouter, createWebHistory } from 'vue-router'
import QuizList from '../components/QuizList.vue'
import Quiz from '../components/Quiz.vue'
import Result from '../components/Result.vue'

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
    component: Result,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
