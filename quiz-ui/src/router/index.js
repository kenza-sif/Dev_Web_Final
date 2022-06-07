import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NewQuizPage from '../views/NewQuizPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/start-new-quiz-page',
      name: 'start-new-quiz-page',
      component: () => import('../views/NewQuizPage.vue')
    },
    {
      path: '/questions',
      name: 'questions',
      component: () => import('../views/QuestionManager.vue')
    },
    {
      path: '/Score',
      name: 'Score',
      component: () => import('../views/Score.vue')
    }
  ]
})

export default router
