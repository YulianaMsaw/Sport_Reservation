import Vue from 'vue'
import VueRouter from 'vue-router'
import LK from './pages/lk.vue'
import Trainer from './pages/trainer.vue'
import Complex from './pages/complex.vue'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes = [
        { path: '/', name: 'Home', component: Home },
        {
          path: '/lk',
          name: 'LK',
          component: LK,
          meta: {
            requiresAuth: true
          }
        },
        { path: '/trainer', name: 'Trainer', component: Trainer },
        { path: '/complex', name: 'Complex', component: Complex }
      ]
})