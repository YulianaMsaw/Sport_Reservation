import './assets/main.css'
import { createRouter, createWebHistory } from 'vue-router'
import { createApp } from 'vue'
import App from './App.vue'
import Home from './pages/home.vue'
import LK from './pages/lk.vue'
import Trainer from './pages/trainer.vue'
import Complex from './pages/complex.vue'
import store from './store'
import signin from './pages/signin.vue'
import registration from './pages/registration.vue'
import User from './pages/user.vue'
import ProfileEdit from './pages/profileEdit.vue'
import Search from './pages/search.vue'

const app = createApp(App)

const routes = [
  { path: '/', name: 'Home', component: Home },
  {
    path: '/lk',
    name: 'LK',
    component: LK,
    meta: {
      requiresAuth: true
    }
  },
  { path: '/trainer/:id', name: 'Trainer', component: Trainer },
  { path: '/signin', name: 'Signin', component: signin },
  { path: '/registration', name: 'Registration', component: registration },
  { path: '/complex/:id', name: 'Complex', component: Complex },
  { path: '/user/:id', name: 'User', component: User },
  { path: '/edit', name: 'Profile Edit', component: ProfileEdit },
  { path: '/search', name: 'Search', component: Search }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

app.use(router)
app.use(store)
app.mount('#app')
