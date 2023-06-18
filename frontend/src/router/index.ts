import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Homes from '@/pages/home/index.vue'
import Home from '@/components/home/home.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/login',
    name: 'login',
    component: Homes
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
