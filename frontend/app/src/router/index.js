import Vue from 'vue'
import Router from 'vue-router'
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Home from '@/views/Home'
import Character from '@/views/Character'
import Report from '@/views/Report'
import Signin from '@/views/Sign in'
import Mde from '@/views/Mde'
import VueSimplemde from 'vue-simplemde'
import 'simplemde/dist/simplemde.min.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.prototype.$axios = axios

Vue.use(BootstrapVue)
Vue.use(BootstrapVueIcons)
Vue.use(VueAxios, axios)
Vue.use(Router)
Vue.use(VueSimplemde)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signin,
      props: {
        signup: true
      }
    },
    {
      path: '/signin',
      name: 'signin',
      component: Signin,
      props: {
        signup: false
      }
    },
    {
      path: '/character',
      name: 'character',
      component: Character,
      props: true
    },
    {
      path: '/report',
      name: 'report',
      component: Report,
      props: true
    },
    {
      path: '/test',
      name: 'test',
      component: Mde
    }
  ]
})
