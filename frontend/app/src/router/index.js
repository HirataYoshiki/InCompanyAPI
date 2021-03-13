import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import Router from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import HelloWorld from '@/components/HelloWorld'
import Signin from '@/components/Sign in'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.prototype.$axios = axios   

Vue.use(VueAxios, axios)
Vue.use(Router)
Vue.use(BootstrapVue)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/signin',
      name: 'signin',
      component: Signin
    }
  ]
})
