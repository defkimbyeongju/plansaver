import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue/'
import MapView from '@/views/MapView.vue/'
import ArticleView from '@/views/ArticleView.vue/'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import ProductsView from '@/views/ProductsView.vue/'
import ProfileView from '@/views/ProfileView.vue/'
import SignUpView from '@/views/SignUpView.vue/'
import LoginView from '@/views/LoginView.vue/'
import ExchangeView from '@/views/ExchangeView.vue/'
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/article',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView
    },
    {
      path: '/products/deposits',
      name: 'deposits',
      component: DepositList
    },
    {
      path: '/products/savings',
      name: 'savings',
      component: SavingList
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
  ]
})

export default router
